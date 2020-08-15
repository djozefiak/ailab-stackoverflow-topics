import keras.backend as K

def precision(y_true, y_pred):
	true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
	predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
	pre = true_positives / (predicted_positives + K.epsilon())
	return pre

def recall(y_true, y_pred):
	true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
	possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
	rec = true_positives / (possible_positives + K.epsilon())
	return rec

def f1_score(y_true, y_pred):
	pre = precision(y_true, y_pred)
	rec = recall(y_true, y_pred)
	f1 = 2 * ((pre * rec) / (pre + rec + K.epsilon()))
	return f1

def f1_loss(y_true, y_pred):
	true_positives = K.sum(K.cast(y_true * y_pred, "float"), axis=0)
	true_negatives = K.sum(K.cast((1 - y_true) * (1 - y_pred), "float"), axis=0)
	false_positives = K.sum(K.cast((1 - y_true) * y_pred, "float"), axis=0)
	false_negatives = K.sum(K.cast(y_true * (1 - y_pred), "float"), axis=0)

	pre = true_positives / (true_positives + false_positives + K.epsilon())
	rec = true_positives / (true_positives + false_negatives + K.epsilon())

	f1 = 2 * pre * rec / (pre + rec + K.epsilon())
	f1 = tf.where(tf.math.is_nan(f1), tf.zeros_like(f1), f1)
	return 1 - K.mean(f1)
