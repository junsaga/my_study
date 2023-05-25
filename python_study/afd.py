from sklearn.datasets import load_breast_cancer

cancer =load_breast_cancer()

X_train, X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify =cancer.targetm
                                                  random_state=42)
n_features =cancer.data.shape[1]

score_n_tr_est =[]
score_n_te_est =[]
score_m_tr_mft =[]
score_m_te_mft =[]

for i in np.arange(1,n_features+1)

    params_n ={'n_estimators':i 'max_features'}