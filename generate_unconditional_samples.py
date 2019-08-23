#!/usr/bin/env python3

import json
import os
import numpy as np
import tensorflow as tf
import model
import sample
import encoder


class GenerateUnconditionalSamples:
    def __init__(self):
        return

    def sample_model(
            self,
            model_name='124M',
            seed=None,
            nsamples=1,
            batch_size=1,
            length=250,
            temperature=1,
            top_k=0,
            models_dir=os.path.abspath('models')):
        """
        Run the sample_model
        :model_name=124M : String, which model to use
        :seed=None : Integer seed for random number generators, fix seed to
         reproduce results
        :nsamples=0 : Number of samples to return, if 0, continues to
         generate samples indefinately.
        :batch_size=1 : Number of batches (only affects speed/memory).
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
        #models_dir = os.path.abspath('models')
        enc = encoder.get_encoder(model_name, models_dir)
        hparams = model.default_hparams()
        with open('{}/{}/hparams.json'.format(models_dir, model_name)) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            np.random.seed(seed)
            tf.set_random_seed(seed)

            output = sample.sample_sequence(
                hparams=hparams, length=length,
                start_token=enc.encoder['<|endoftext|>'],
                batch_size=batch_size,
                temperature=temperature, top_k=top_k
            )[:, 1:]

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint('/{}/{}'.format(models_dir,model_name))
            saver.restore(sess, ckpt)
            generated = 0
            while nsamples == 0 or generated < nsamples:
                out = sess.run(output)
                for i in range(batch_size):
                    generated += batch_size
                    text = enc.decode(out[i])
                    return "'" + text + "'"

