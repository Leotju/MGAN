from coco import COCO
from eval_MR_multisetup import COCOeval

annType = 'bbox'  # specify type here
print('Running demo for *%s* results.' % (annType))

# initialize COCO ground truth api
annFile = 'eval/val_gt.json'
# initialize COCO detections api
resFile = 'result/50_65.pkl.json'

## running evaluation
res_file = open("eval/results.txt", "w")
for id_setup in range(0, 2):
    cocoGt = COCO(annFile)
    cocoDt = cocoGt.loadRes(resFile)
    imgIds = sorted(cocoGt.getImgIds())
    cocoEval = COCOeval(cocoGt, cocoDt, annType)
    cocoEval.params.imgIds = imgIds
    cocoEval.evaluate(id_setup)
    cocoEval.accumulate()
    cocoEval.summarize(id_setup, res_file)

res_file.close()
