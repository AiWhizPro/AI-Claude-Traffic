param(
    [Parameter(Mandatory=$true)]
    [string]$Keyword
)

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectRoot
$venvPython = Join-Path $projectRoot 'venv\Scripts\python.exe'
if (Test-Path $venvPython) {
    & $venvPython .\futuretech\manage.py write_a_blog "$Keyword"
} else {
    python .\futuretech\manage.py write_a_blog "$Keyword"
}
