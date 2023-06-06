import numpy as np
import pandas as pd
from io import StringIO
import altair as alt
import sys
import itertools
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


@st.cache_data 
def get_data(filepath) -> pd.DataFrame:
    """
    ファイルを読み込む。st.cache内であれば、この関数が下で呼び出されるときに
    もう一度読み込まれることはなくなる（ただし、関数自体や引数自体が変わったら変わってくれる）。
    """
    df = pd.read_csv(filepath, sep='\t')
    assert isinstance(df, pd.DataFrame) # 絶対データフレームしか渡していないことを確認する行
    return df


X_train = get_data('./train.feature.txt')
X_valid = get_data('./valid.feature.txt')
X_test = get_data('./test.feature.txt')

y_train = pd.read_csv('./train.txt', sep='\t')['category']
y_valid = pd.read_csv('./valid.txt', sep='\t')['category']
y_test = pd.read_csv('./test.txt', sep='\t')['category']

#st.write(train.head(10))

st.header('52. 学習')
model = LogisticRegression(max_iter=1000) #ロジスティックモデルのインスタンスを作成

@st.cache_data
def training():
    logistic_model = model.fit(X_train, y_train) # ロジスティックモデルの重み付け（特徴量を出力ラベルに変換する重みを見つける）の学習
    return logistic_model

logistic_model = training()

st.header('53. 予測')

def predict(lm, X):
    preds = lm.predict(X)
    probs = np.max(lm.predict_proba(X), axis=1)
    return preds, probs


st.text('>学習データでの予測')
train_preds, train_probs = predict(logistic_model, X_train)
train_predicts = pd.DataFrame([[pre, pro] for pre, pro in zip(train_preds, train_probs)], columns = ['予測', '確率'])
st.write(train_predicts)

st.text('>評価データでの予測')

test_preds, test_probs = predict(logistic_model, X_test)
test_predicts = pd.DataFrame([[pre, pro] for pre, pro in zip(test_preds, test_probs)], columns = ['予測', '確率'])
st.write(test_predicts)

# 予測確率ってどう出しているのか？

st.header('54. 正解率の計測')
#pred_train = logistic_model.predict(train)
#pred_test = logistic_model.predict(test)

st.write('学習データの正解率:', accuracy_score(y_train, train_preds))
st.write('評価データの正解率:', accuracy_score(y_test, test_preds))

st.header('55. 混同行列の作成')

def cm_produce(y, preds):
    labels = ['b', 'e', 'm', 't']
    cm = confusion_matrix(y, preds, labels=labels)
    columns_labels = ["pred_" + str(l) for l in labels]
    index_labels = ["act_" + str(l) for l in labels]
    cm = pd.DataFrame(cm, columns=columns_labels, index=index_labels)
    return cm

labels = ['b', 'e', 'm', 't']
matrix_train = confusion_matrix(y_train, train_preds, labels=labels)
columns_labels = ["pred_" + str(l) for l in labels]
index_labels = ["act_" + str(l) for l in labels]
matrix_train = pd.DataFrame(matrix_train, columns=columns_labels, index=index_labels)
matrix_test = cm_produce(y_test, test_preds)

st.write('学習データの混同行列', matrix_train)
st.write('評価データの混同行列', matrix_test)

st.header('56. 適合率，再現率，F1スコアの計測')
# sklearn.metrics からclassfication_reportをインポート

rates_and_scores = classification_report(y_test, test_preds, labels=['b', 'e', 'm', 't'])
#rates_and_scores = rates_and_scores.pd.DataFrame([x.split('\t') for x in rates_and_scores.split('\n')])
#rates_and_scores = pd.DataFrame(classification_report, index=None)
st.text(rates_and_scores)

st.header('57. 特徴量の重みの確認')

st.write(X_train.head(10))
features = X_train.columns.values

index = [i for i in range(1, 11)]
for c, coef in zip(logistic_model.classes_, logistic_model.coef_):
  st.write(f'【カテゴリ】{c}')
  best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['上位'], index=index).T
  worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['下位'], index=index).T
  st.write(pd.concat([best10, worst10], axis=0))
  st.write('\n')

st.header('58. 正則化パラメータの変更')


cs = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]
@st.cache_data
def training_change_c(train_data, y_data):
    ac_score = []
    for c in cs:
        model = LogisticRegression(C=c, random_state=0, max_iter = 10000)
        model.fit(X_train, y_train)
        ac_score.append(accuracy_score(y_data, model.predict(train_data)))
    return ac_score

train_ac_score = training_change_c(X_train, y_train)
valid_ac_score = training_change_c(X_valid, y_valid)
test_ac_score = training_change_c(X_test, y_test)

train_ac_df = pd.DataFrame(list(zip(['train'] * 8, cs, train_ac_score)), columns=['data', 'cs','accuracy_score'])
valid_ac_df = pd.DataFrame(list(zip(['valid'] * 8, cs, valid_ac_score)), columns=['data', 'cs','accuracy_score'])
test_ac_df = pd.DataFrame(list(zip(['test'] * 8, cs, test_ac_score)), columns=['data', 'cs','accuracy_score'])
df = pd.concat([train_ac_df, valid_ac_df, test_ac_df], axis=0)
st.write(df)

chart = alt.Chart(df).mark_line(
        ).encode(
                x=alt.X('cs:N', title='パラメータ'),
                y=alt.Y('accuracy_score:Q', title='正解率'),
                color=alt.Color('data:N', title='データ')
                ).properties(
                    title='パラメータと正解率の関係')

st.altair_chart(chart, use_container_width=True)

st.header('59. ハイパーパラメータの探索')

@st.cache_data
def accuracy_scores(c, sl, cw):
    model = LogisticRegression(C=c, solver=sl, class_weight=cw, random_state=0)
    model.fit(X_train, y_train)
    test_pred = model.predict(X_test)
    scores = accuracy_score(y_test, test_pred)
    return scores

cs=[0.01, 0.1, 1, 10, 100, 1000]
sls = ['lbfgs', 'liblinear', 'sag', 'saga']
cws = [None, 'balanced']

parameter_scores = {}

for c, sl, cw in itertools.product(cs, sls, cws):
    parameters = sl + '-' + str(c)
    scores = accuracy_scores(c, sl, cw)
    parameter_scores[parameters] = scores

st.text('> パラメータの組み合わせと正解率')
st.write(parameter_scores)
st.text('> 最も良い正解率を出すパラメータの組み合わせ')
st.write(max(parameter_scores, key=parameter_scores.get), ':', max(parameter_scores.values()))
