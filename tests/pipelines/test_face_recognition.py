# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

import numpy as np

from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.utils.test_utils import test_level


class FaceRecognitionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.task = Tasks.face_recognition
        self.model_id = 'damo/cv_ir101_facerecognition_cfglint'

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_face_compare(self):
        img1 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_1.png'
        img2 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_2.png'

        face_recognition = pipeline(
            Tasks.face_recognition, model=self.model_id)
        emb1 = face_recognition(img1)[OutputKeys.IMG_EMBEDDING]
        emb2 = face_recognition(img2)[OutputKeys.IMG_EMBEDDING]
        sim = np.dot(emb1[0], emb2[0])
        print(f'Cos similarity={sim:.3f}, img1:{img1}  img2:{img2}')

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_face_compare_use_det(self):
        img1 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_1.png'
        img2 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_2.png'

        face_recognition = pipeline(
            Tasks.face_recognition, model=self.model_id, use_det=True)
        emb1 = face_recognition(img1)[OutputKeys.IMG_EMBEDDING]
        emb2 = face_recognition(img2)[OutputKeys.IMG_EMBEDDING]
        sim = np.dot(emb1[0], emb2[0])
        print(f'Cos similarity={sim:.3f}, img1:{img1}  img2:{img2}')

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_face_compare_not_use_det(self):
        img1 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_1.png'
        img2 = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/face_recognition_2.png'

        face_recognition = pipeline(
            Tasks.face_recognition, model=self.model_id, use_det=False)
        emb1 = face_recognition(img1)[OutputKeys.IMG_EMBEDDING]
        emb2 = face_recognition(img2)[OutputKeys.IMG_EMBEDDING]
        sim = np.dot(emb1[0], emb2[0])
        print(f'Cos similarity={sim:.3f}, img1:{img1}  img2:{img2}')


if __name__ == '__main__':
    unittest.main()
