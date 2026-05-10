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

# Limpiar y re-subir todo de forma atómica
ssh $SERVER "rm -rf $REMOTE/* && mkdir -p $REMOTE/css $REMOTE/js $REMOTE/assets" | Out-Null
$result = scp -r "${LOCAL}/*" "${SERVER}:${REMOTE}/" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR en scp: $result"
    exit 1
}
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
