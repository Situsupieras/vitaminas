#!/usr/bin/env pwsh
# deploy.ps1 — Sube landing_esvitamina/ al VPS y la deja live en /vitaminas/
# Uso: .\deploy.ps1 [-Version "3.1.3"]

param([string]$Version = "")

$SERVER  = "sts@148.230.88.220"
$LOCAL   = "landing_esvitamina"
$REMOTE  = "/home/sts/vitaminas-landing"
$URL     = "https://tiendasts.com/vitaminas/"

# Bump cache-buster en index.html si se pasa -Version
if ($Version -ne "") {
    $html = Get-Content "$LOCAL/index.html" -Raw
    $html = $html -replace '\?v=[\d.]+', "?v=$Version"
    Set-Content "$LOCAL/index.html" $html -NoNewline
    Write-Host "Cache-buster bumpeado a v=$Version"
}

Write-Host "Deployando Es Vitamina -> $URL"

# Limpiar y recrear estructura en VPS
ssh $SERVER "rm -rf $REMOTE/* && mkdir -p $REMOTE/css $REMOTE/js $REMOTE/assets" | Out-Null

# Subir archivos explícitamente por directorio (scp -r con wildcards no funciona en PowerShell)
$uploads = @(
    @{ src="$LOCAL/index.html";   dst="$REMOTE/index.html" },
    @{ src="$LOCAL/robots.txt";   dst="$REMOTE/robots.txt" },
    @{ src="$LOCAL/sitemap.xml";  dst="$REMOTE/sitemap.xml" },
    @{ src="$LOCAL/css/variables.css";  dst="$REMOTE/css/variables.css" },
    @{ src="$LOCAL/css/components.css"; dst="$REMOTE/css/components.css" },
    @{ src="$LOCAL/css/sections.css";   dst="$REMOTE/css/sections.css" },
    @{ src="$LOCAL/css/responsive.css"; dst="$REMOTE/css/responsive.css" },
    @{ src="$LOCAL/js/quiz.js";    dst="$REMOTE/js/quiz.js" },
    @{ src="$LOCAL/js/ui.js";     dst="$REMOTE/js/ui.js" },
    @{ src="$LOCAL/js/smooth.js"; dst="$REMOTE/js/smooth.js" },
    @{ src="$LOCAL/assets/guia-sintomas-esvitamina.html"; dst="$REMOTE/assets/guia-sintomas-esvitamina.html" },
    @{ src="$LOCAL/assets/og-image.html"; dst="$REMOTE/assets/og-image.html" }
)
$errors = 0
foreach ($u in $uploads) {
    scp $u.src "${SERVER}:$($u.dst)" 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) { Write-Host "  ERROR: $($u.src)"; $errors++ }
    else { Write-Host "  OK  $($u.src)" }
}
if ($errors -gt 0) { Write-Host "Deploy falló con $errors error(es)."; exit 1 }
Write-Host "  OK  todos los archivos subidos"

# Reiniciar nginx para limpiar caché
ssh $SERVER "docker restart vitaminas-landing" | Out-Null
Write-Host "  OK  nginx reiniciado"

# Verificar version en produccion
$check = ssh $SERVER "curl -s $URL | grep -o 'v=[0-9.]*' | head -1"
Write-Host ""
Write-Host "Version en produccion: $check"

$status = ssh $SERVER "curl -sI $URL | head -1"
Write-Host "HTTP status: $status"
Write-Host ""
Write-Host "Landing actualizada en $URL"
