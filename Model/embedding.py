"""
*************************************************************
*                                                           *
*    Deep Neural Network Recommendation System for Yelp     *
*                                                           *
*************************************************************

Embedding data:

"""

import math
import numpy as np
import tensorflow as tf
from Model.main import config
from tensorflow.contrib.tensorboard.plugins import projector


class Embedding:
    def __init__(self, data, size):
        self.data = data
        self.batch_size = 0
        self.__build(size)

    def __generate_batch(self, num_skips, skip_window):
        train_input = []
        train_label = []
        count = 0
        for key, value in self.data.items():
            if len(value) <= 1:
                count += 1
                print("Warning batch_size 0", key, count)
                continue
            for i in range(len(value)):
                # Find the possible index within the window
                lower_bound = i - skip_window
                upper_bound = i + skip_window + 1
                if lower_bound < 0:
                    lower_bound = 0
                if upper_bound > len(value):
                    upper_bound = len(value)
                context_id = [index for index in range(lower_bound, upper_bound) if index != i]
                self.batch_size += len(context_id)
                for j in context_id:
                    train_input.append(value[i])
                    train_label.append([value[j]])
        return train_input, train_label

    def __build(self, size):

        # Generate input batch
        inputs, labels = self.__generate_batch(config.num_skips, config.skip_window)

        # Placeholders for inputs
        train_inputs = tf.placeholder(tf.int32, shape=[self.batch_size])
        train_labels = tf.placeholder(tf.int32, shape=[self.batch_size, 1])

        # Look up embeddings for inputs.
        # Random initialize
        embeddings = tf.Variable(
            tf.random_uniform([size, config.embedding_size], -1.0, 1.0))

        # Initialize weight and biases
        nce_weights = tf.Variable(
            tf.truncated_normal([size, config.embedding_size],
                                stddev=1.0 / math.sqrt(config.embedding_size)))
        nce_biases = tf.Variable(tf.zeros([size]))

        embed = tf.nn.embedding_lookup(embeddings, train_inputs)

        # Compute the NCE loss, using a sample of the negative labels each time.
        loss = tf.reduce_mean(
            tf.nn.nce_loss(weights=nce_weights,
                           biases=nce_biases,
                           labels=train_labels,
                           inputs=embed,
                           num_sampled=config.num_sampled,
                           num_classes=size))

        # Add the loss value as a scalar to summary.
        # tf.summary.scalar('loss', loss)

        # Use the SGD optimizer.
        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)

        # begin to train
        num_steps = config.num_steps

        # Add variable initializer.
        init = tf.global_variables_initializer()

        with tf.Session() as session:
            init.run()
            print('Initialized')

            average_loss = 0
            for step in range(num_steps):
                feed_dict = {train_inputs: inputs, train_labels: labels}
                _, cur_loss = session.run([self.optimizer, loss], feed_dict=feed_dict)

                average_loss += cur_loss

                if step % 20 == 0:
                    if step > 0:
                        average_loss /= 20
                    # The average loss is an estimate of the loss over the last 2000
                    # batches.
                    print('Average loss at step ', step, ': ', average_loss)
                    average_loss = 0

        final_embeddings = embeddings.eval()

    def get_embed(self):

        return


