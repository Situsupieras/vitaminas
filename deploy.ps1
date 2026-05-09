#!/usr/bin/env pwsh
# deploy.ps1 — Sube landing_esvitamina/ al VPS y la deja live en /vitaminas/

$SERVER  = "sts@148.230.88.220"
$LOCAL   = "landing_esvitamina"
$REMOTE  = "/home/sts/vitaminas-landing"
$URL     = "https://tiendasts.com/vitaminas/"

$files = @(
    @{ src = "$LOCAL/index.html";            dst = "$REMOTE/index.html" },
    @{ src = "$LOCAL/robots.txt";            dst = "$REMOTE/robots.txt" },
    @{ src = "$LOCAL/sitemap.xml";           dst = "$REMOTE/sitemap.xml" },
    @{ src = "$LOCAL/css/variables.css";     dst = "$REMOTE/css/variables.css" },
    @{ src = "$LOCAL/css/components.css";    dst = "$REMOTE/css/components.css" },
    @{ src = "$LOCAL/css/sections.css";      dst = "$REMOTE/css/sections.css" },
    @{ src = "$LOCAL/css/responsive.css";    dst = "$REMOTE/css/responsive.css" },
    @{ src = "$LOCAL/js/quiz.js";            dst = "$REMOTE/js/quiz.js" },
    @{ src = "$LOCAL/js/ui.js";              dst = "$REMOTE/js/ui.js" },
    @{ src = "$LOCAL/js/smooth.js";          dst = "$REMOTE/js/smooth.js" },
    @{ src = "$LOCAL/assets/guia-sintomas-esvitamina.html"; dst = "$REMOTE/assets/guia-sintomas-esvitamina.html" },
    @{ src = "$LOCAL/assets/og-image.html";  dst = "$REMOTE/assets/og-image.html" }
)

Write-Host "Deployando Es Vitamina -> $URL"

$errors = 0
foreach ($f in $files) {
    $result = scp $f.src "${SERVER}:$($f.dst)" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ERROR: $($f.src) -> $($f.dst)"
        Write-Host "  $result"
        $errors++
    } else {
        Write-Host "  OK  $($f.src)"
    }
}

if ($errors -gt 0) {
    Write-Host ""
    Write-Host "Deploy completado con $errors error(es). Revisá arriba."
    exit 1
}

$status = ssh $SERVER "curl -sI $URL | head -1"
Write-Host ""
Write-Host "Verificacion: $status"
Write-Host ""
Write-Host "Landing actualizada en $URL"
