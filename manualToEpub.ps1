pandoc `
    --metadata title="Anki Manual 20201222" `
    --filter ..\fix-links-single-file.py `
    -s $(cat ..\pandocIncludes.txt) `
    -f markdown-raw_tex `
    -t epub `
    -o ..\AnkiManual-20201222.epub