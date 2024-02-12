import os 

# TODO: look over them
#CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
#PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
#PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
#TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
#LABEL_MAP_NAME = 'label_map.pbtxt'

# TODO: should be past as an agrument
TRAINING_FOLDER = 'training_hand_gestures'



file_name = {
    'LABEL_MAP': 'label_map.pbtxt',
    'TEST_RECORD': 'test.record',
    'TRAIN_RECORD': 'train.record',
}

folder_name = {
    'ANNOTATIONS': 'annotations',
    'EXPORTED_MODELS': 'exported-models',
    'IMAGES': 'images',
    'COLLECTED_IMAGES': 'collectedimages',
    'TRAIN': 'train',
    'TEST': 'test',
    'MODELS': 'models',
    'PRETRAINED_MODELS': 'pre-trained-models'
}

# Relative paths in training folder
paths = {
    'ANNOTATIONS_PATH': os.path.join(TRAINING_FOLDER, folder_name['ANNOTATIONS']),
    'EXPORTED_MODELS_PATH': os.path.join(TRAINING_FOLDER, folder_name['EXPORTED_MODELS']),
    'IMAGES_PATH': os.path.join(TRAINING_FOLDER, folder_name['IMAGES']),
    'COLLECTED_IMAGES_PATH': os.path.join(TRAINING_FOLDER, folder_name['IMAGES'], folder_name['COLLECTED_IMAGES']),
    'TRAIN_PATH': os.path.join(TRAINING_FOLDER, folder_name['IMAGES'], folder_name['TRAIN']),
    'TEST_PATH': os.path.join(TRAINING_FOLDER, folder_name['IMAGES'], folder_name['TEST']),
    'MODELS_PATH': os.path.join(TRAINING_FOLDER, folder_name['MODELS']),
    'PRETRAINED_MODELS_PATH': os.path.join(TRAINING_FOLDER, folder_name['PRETRAINED_MODELS'])
 }

files = {
    'LABEL_MAP': os.path.join(paths['ANNOTATIONS_PATH'], file_name['LABEL_MAP']),
    'TEST_RECORD': os.path.join(paths['ANNOTATIONS_PATH'], file_name['TEST_RECORD']),
    'TRAIN_RECORD': os.path.join(paths['ANNOTATIONS_PATH'], file_name['TRAIN_RECORD']),
}

# TODO: this is just for actual learning should have a seperate one of images and stuff
#paths = {
#    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
#    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
#    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
#    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
#    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
#    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
#    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
#    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME), 
#    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'), 
#    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfjsexport'), 
#    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfliteexport'), 
#    'PROTOC_PATH':os.path.join('Tensorflow','protoc')
# }

#files = {
#    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
#    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
#    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
#}
