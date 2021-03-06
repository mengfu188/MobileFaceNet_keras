import argparse

import tensorflow as tf
keras = tf.keras
K = tf.keras.backend

from nets.net import prelu


def get_arg():
    parser = argparse.ArgumentParser(description='convert .h5 to .tflite')
    parser.add_argument('--h5_file', help='h5 file to convert')
    parser.add_argument('--tflite_file', help='tflite file to save')
    return parser.parse_args()


def _main(args):
    """
    use demo

    ```shell
    python convert_tflite.py \
    --h5_file output/model.h5 \
    --tflite_file output/model.tflite
    ```
    :param args: arguments with --h5_file and --tflite_file
    :return:
    """
    # model = keras.models.load_model(args.h5_file, custom_objects={'prelu': prelu})
    with tf.keras.utils.custom_object_scope({'prelu': prelu}):
        converter = tf.lite.TFLiteConverter.from_keras_model_file(args.h5_file)
        tflite_file = converter.convert()
        open(args.tflite_file, 'wb').write(tflite_file)
    print('='*30)
    print('tffile file save in {}.'.format(args.tflite_file))


if __name__ == '__main__':
    _main(get_arg())
