one_hot = True 
embedding_size = 256  # is ignored if one_hot=True
num_layers = 3
rnn_size = 512
dropout = 0.5

learning_rate = 0.001 # originally 0.003
learning_rate_decay_after = 10 # originally 20
learning_rate_decay = 0.97

batch_size = 32
max_epoch = 300
grad_clipping = 5
validation_fraction = 0.05
validate_every = 148 # iterations / originally 500

save_every = 1  # epochs / originally 10 lol

# resume_path = 'metadata/configSample-DutchIrish2C-20250122-170828.pkl' # include this to resume training
# resume_path = 'metadata/configSample-DutchIrish2C-20250123-142707.pkl' # This is the new one !!!
# resume_path = 'metadata/configSample-DutchIrish2C-20250124-094933.pkl' # 1/24/2025
# resume_path = 'metadata/configSample-DutchIrish2C-20250124-170722.pkl' # 1/24/2025 24 epoch
resume_path =  'metadata/configSample-DutchIrish2C-20250125-101321.pkl' # 1/25/2025 30 epoch
