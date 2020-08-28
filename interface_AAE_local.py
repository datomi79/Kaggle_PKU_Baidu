import numpy as np
from interface_utils import init_model, inference_detector, format_return_data, projective_distance_estimation_AAE
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '4'

model, cfg = init_model()


def main():
    image_path = "./upload_imgs/tmp_{}.jpg".format(5960)
    result = inference_detector(cfg, model, image_path)
    data = format_return_data(result)

    if data.shape[0] > 0:
        data = data[0]
        json = dict(
            code=0,
            msg='success',
            x1=data[0],
            y1=data[1],
            x2=data[2],
            y2=data[3],
            conf=data[4],
            rotation=list(data[5:8]),
            translation=list(data[8:]),
        )
        # We obtain the car 3D information here
        # A demo
        camera_matrix = np.array([[493.90, 0, 318.69],
                                  [0, 493.81, 240.39],
                                  [0, 0, 1]], dtype=np.float32)
        ZRENDER = 0.2
        SCALE = 0.04

        t_pred_x, t_pred_y, t_pred_z = projective_distance_estimation_AAE(json, image_path, camera_matrix, ZRENDER,
                                                                          SCALE,
                                                                          draw=True)
        json['t_pred_x'] = t_pred_x
        json['t_pred_y'] = t_pred_y
        json['t_pred_z'] = t_pred_z

    else:
        json = dict(status=1, msg='NO CAR')

    return json


if __name__ == '__main__':
    main()
