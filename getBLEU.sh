python translate.py
./postprocess.sh model_translations.txt model_translations.out en
cat model_translations.out | sacrebleu baseline/raw_data/test.en
