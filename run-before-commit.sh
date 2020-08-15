#! /bin/bash
# Please run this before any commits that change the builder.py or any addons
rm -r example/building/builder.py
cp builder.py example/building

python3 -m zipfile -c npc.zip addons builder.py
