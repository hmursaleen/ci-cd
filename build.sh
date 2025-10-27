#!/usr/bin/env bash
set -euo pipefail

# Optional: export env vars if you need them here.
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Build finished."
