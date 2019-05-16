import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

data_df = pd.read_csv('./outputs/predict_dev', sep='\t', header=None)
data_df.columns = ["words", "target", "prediction"]
target_list = data_df["target"].tolist()
prediction_list = data_df["prediction"].tolist()
target = np.array(target_list)
prediction = np.array(prediction_list)
labels = list(set(target_list))
classification_report_ = classification_report(target, prediction, labels=labels)

print(classification_report_)
with open("./outputs/crf++_measure_score_report_ner.txt", 'w') as report:
    report.write("<<< IN TEST SET, NAMED ENTITY RECOGNITION TASK REPORT. THE NUMBER OF NER TAGSET IS: " +
                 str(len(labels)) + str(labels) + ">>>\n\n")
    report.write(classification_report_)
report.close()
