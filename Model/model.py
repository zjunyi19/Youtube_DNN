"""
*************************************************************
*                                                           *
*    Deep Neural Network Recommendation System for Yelp     *
*                                                           *
*************************************************************



"""
import tensorflow as tf;
from Model.main import config

class DNNmodel:
    def __init__(self, rev_embed_size, cat_embed_size, business_size):
        self.input_size = rev_embed_size + cat_embed_size
        self.rev_embed_size = rev_embed_size
        self.layer1_size = config.DNN_layer1_size
        self.layer2_size = config.DNN_layer2_size
        self.layer3_size = rev_embed_size
        self.output_size = business_size
        self.optimizer = tf.keras.optimizers.SGD(config.DNN_learning_rate)
        self.loss = 'sparse_categorical_crossentropy'
        self.model = self.__build()




    def  __build(self):
        # Define and build NN model
        layer_1 = tf.keras.layers.dense(self.layer1_size, activation=tf.nn.relu, name='f1')
        layer_1 = tf.nn.dropout(layer_1, keep_prob=self.keep_prob)
        layer_2 = tf.keras.layers.dense(self.layer2_size, activation=tf.nn.relu, name='f2')
        layer_2 = tf.nn.dropout(layer_2, keep_prob=self.keep_prob)
        layer_3 = tf.keras.layers.dense(self.layer3_size, activation=tf.nn.relu, name='f3')
        layer_4 = tf.keras.layers.dense(self.output_size, activation=tf.nn.softmax, name='f4')
        model = tf.keras.Sequential([layer_1, layer_2, layer_3, layer_4])
        model.compile(optimizer=self.optimizer,loss=self.loss,metrics=['accuracy'])
        return model

    def train(self, inputs, labels):
        #TODO: EPOCHS BASED ON ELBOW METHOD
        self.model.fit(inputs, labels, epochs=20)
        loss, acc = self.model.evaluate(inputs, labels)
        print("loss=", loss)
