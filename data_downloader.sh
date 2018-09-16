#!/usr/bin/env bash
# Check kaggle command
kaggle competitions list -s health > /dev/null
if [ $? != 0 ]; then
    echo "Check kaggle command."
    exit
fi 

# Download
echo "---Download---"
kaggle competitions download -p data -c tgs-salt-identification-challenge

echo "---Unzip---"
unzip -qn data/train.zip -d data/train
unzip -qn data/test -d data/test
echo "Finish"

echo "---Delete .zip---"
rm data/train.zip
rm data/test.zip
echo "Finish"