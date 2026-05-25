param(
    [Parameter(Mandatory=$true)]
    [string]$Keyword
)

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectRoot
python .\futuretech\manage.py write_a_blog "$Keyword"
