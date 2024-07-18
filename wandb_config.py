import wandb

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="classifier_kgc",

    # track hyperparameters and run metadata
    config={
    'score_func': 'conve',
    'lr': 0.005,
    'class_num': 100,
    'embed_dim': 200,
    'relation_dim': 100,
    'nhead': 4,
    'batch_size': 512,
    'kill_cut': 100
    }
)