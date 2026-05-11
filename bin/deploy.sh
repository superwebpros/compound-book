#!/usr/bin/env bash
# Render the book (HTML + PDF + EPUB) and deploy _book/ to Cloudflare Pages.
# Production target: https://books.compoundorg.com
#
# Requires:
#   - quarto (https://quarto.org)
#   - xelatex (`brew install --cask mactex` or TinyTeX) for PDF
#   - Brand fonts installed: `brew install --cask font-archivo font-bricolage-grotesque font-jetbrains-mono`
#   - Cloudflare auth: `npx wrangler login` (one-time)

set -euo pipefail

cd "$(dirname "$0")/.."

PROJECT="compound-books"
BRANCH="master"

echo "→ Rendering all formats..."
quarto render

echo "→ Deploying _book/ to Cloudflare Pages project '${PROJECT}' (branch ${BRANCH})..."
npx --yes wrangler@latest pages deploy _book \
  --project-name="${PROJECT}" \
  --branch="${BRANCH}" \
  --commit-dirty=true

echo "→ Done. https://books.compoundorg.com"
