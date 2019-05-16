python BERT_NER.py --task_name="NER" --do_train=True --do_eval=True --do_predict=True \
-data_dir=data/sub_obj_bio_7labels_3.0 --bert_config_file=checkpoint/bert_config.json \
--init_checkpoint=checkpoint/bert_model.ckpt --vocab_file=checkpoint/vocab.txt \
--max_seq_length=128 --train_batch_size=32 --eval_batch_size=16 --predict_batch_size=16 --learning_rate=2e-5 \
--num_train_epochs=4 --output_dir=./output/results_dir/
