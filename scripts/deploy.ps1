Write-Host "Deployment Started"

cd C:\tmp

git pull origin main

Write-Host "Building..."

python manage.py collectstatic --noinput

# iisreset

Write-Host "Deployment Finished"
