#!/usr/bin/env python3

import json
import os
import numpy as np
import tensorflow as tf
import model, sample, encoder
import random

models = os.listdir(os.path.abspath('models'))


class InteractiveConditionalSample:
    def __init__(self, prompt):
        self.prompt = prompt
        return

    def interact_model(
            self,
            model_name=random.choice(models),
            seed=None,
            nsamples=1,
            batch_size=1,
            length=50,
            temperature=1,
            top_k=0,
            models_dir=os.path.abspath('models')):
        """
        Interactively run the model
        :model_name=124M : String, which model to use
        :seed=None : Integer seed for random number generators, fix seed to reproduce
         results
        :nsamples=1 : Number of samples to return total
        :batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
        :length=None : Number of tokens in generated text, if None (default), is
         determined by model hyperparameters
        :temperature=1 : Float value controlling randomness in boltzmann
         distribution. Lower temperature results in less random completions. As the
         temperature approaches zero, the model will become deterministic and
         repetitive. Higher temperature results in more random completions.
        :top_k=0 : Integer value controlling diversity. 1 means only 1 word is
         considered for each step (token), resulting in deterministic completions,
         while 40 means 40 words are considered at each step. 0 (default) is a
         special setting meaning no restrictions. 40 generally is a good value.
         :models_dir : path to parent folder containing model subfolders
         (i.e. contains the <model_name> folder)
        """
        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        enc = encoder.get_encoder(model_name, models_dir)
        hparams = model.default_hparams()
        with open('{}/{}/hparams.json'.format(models_dir, model_name)) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            output = sample.sample_sequence(
                hparams=hparams, length=length,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint('/{}/{}'.format(models_dir, model_name))
            saver.restore(sess, ckpt)

            context_tokens = enc.encode(self.prompt)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    text = enc.decode(out[i])
                    return self.prompt + text + ' #gpt2'
