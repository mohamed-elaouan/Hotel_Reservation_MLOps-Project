from scipy.stats import randint,uniform 

# In this part of we define the parameters for the models we want( after the testing them) to use in our project. 

LIGHTGBM_PARAMS = {
    'n_estimators': randint(100, 500),
    'learning_rate': uniform(0.01, 0.3),
    'num_leaves': randint(20, 150),
    'max_depth': randint(5,50),
    # 'min_child_samples': randint(10, 100),
    'boosting_type': ['gbdt', 'dart', 'goss']
}

RANDOM_SEARCH_PARAMS = {
    'n_iter' : 2,
    'cv' : 2,
    'n_jobs':-1,
    'verbose' :2,
    'random_state' : 42,
    'scoring' : 'accuracy'
}