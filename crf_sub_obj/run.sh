cd ./data
cat ./ontonote_data/onto.development.ner ./ontonote_data/onto.test.ner > ./test_4columns
cp  ./ontonote_data/onto.train.ner ./train_4columns
python data_helper.py
cd ../
./crf_learn.sh
./crf_test.sh
python calc_f1_score.py