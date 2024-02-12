FROM "tensorflow/tensorflow"
# https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#downloading-the-tensorflow-model-garden

RUN apt update 

RUN mkdir TensorFlow

WORKDIR /TensorFlow

RUN wget https://github.com/tensorflow/models/archive/master.zip
RUN unzip master.zip
RUN mv models-master models
RUN apt -y install protobuf-compiler


WORKDIR /TensorFlow/models/research

RUN protoc object_detection/protos/*.proto --python_out=.

RUN cp object_detection/packages/tf2/setup.py .
RUN python -m pip install .

RUN python object_detection/builders/model_builder_tf2_test.py


WORKDIR /TensorFlow

RUN mkdir workspace


WORKDIR /

COPY requirements-docker-container.txt /TensorFlow/workspace
#RUN pip install -r /TensorFlow/workspace/requirements-container.txt

COPY scripts/preprocessing/generate_tfrecord.py /TensorFlow/workspace

#python generate_tfrecord.py -x /TensorFlow/workspace/training_hand_gestures/images/train -l /TensorFlow/workspace/training_hand_gestures/annotations/label_map.pbtxt -o /TensorFlow/workspace/training_hand_gestures/annotations/train.record
#python generate_tfrecord.py -x /TensorFlow/workspace/training_hand_gestures/images/test -l /TensorFlow/workspace/training_hand_gestures/annotations/label_map.pbtxt -o /TensorFlow/workspace/training_hand_gestures/annotations/test.record 
#cp /TensorFlow/models/research/object_detection/model_main_tf2.py .
#apt install libgl1-mesa-glx
#python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config
#/usr/local/lib/python3.11/dist-packages/tf_slim/data/tfexample_decoder.py .

# TODO: copy post proccessing scripts
# TODO: run preproccessing scripts
# TODO: run learning
# TODO: run post proccessing scripts
