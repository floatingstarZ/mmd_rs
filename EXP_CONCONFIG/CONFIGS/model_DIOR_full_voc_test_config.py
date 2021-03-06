root = '.'
def gen_dict(name, config,
             result_root='/home/huangziyue/data/mmdet_results',
             epoch=12,
             result_name='results.pkl'):
    work_dir = result_root + '/' + name

    return dict(
        ## name修饰
        name=name + '_voc',
        config=config,
        work_dir=  work_dir,
        cp_file=   work_dir+'/epoch_%d.pth' % epoch,
        result=    work_dir+'/epoch_12_' + result_name,
        Task2_results = None,
        Task2_results_split = None,
        eval_results= work_dir + '/epoch_12_voc_eval_results.txt',
        bbox_type='HBB'
    )

DIOR_root = './DOTA_configs/DIOR_voc_test'
DIOR_voc_cfgs = [
    gen_dict('DIOR_retinanet_full',
             DIOR_root + '/' + 'retinanet_r50_fpn_2x.py'),
    gen_dict('DIOR_atss_full',
             DIOR_root + '/' + 'atss_r50_fpn_2x.py'),
    gen_dict('DIOR_cascade_rcnn_full',
             DIOR_root + '/' + 'cascade_rcnn_r50_fpn.py'),
    gen_dict('DIOR_faster_rcnn_full',
             DIOR_root + '/' + 'faster_rcnn_r50_fpn_2x.py'),
    gen_dict('DIOR_fcos_full',
             DIOR_root + '/' + 'fcos_r50_caffe_fpn_4x4_2x.py'),
    gen_dict('DIOR_fovea_full',
             DIOR_root + '/' + 'fovea_r50_fpn_4x4_2x.py'),
    gen_dict('DIOR_fsaf_full',
             DIOR_root + '/' + 'fsaf_r50_fpn_2x.py'),
    gen_dict('DIOR_gfl_full',
             DIOR_root + '/' + 'gfl_r50_fpn_2x.py'),
    gen_dict('DIOR_reppoints_full',
             DIOR_root + '/' + 'reppoints_moment_r50_fpn_2x.py'),
    gen_dict('DIOR_sabl_faster_rcnn_full',
             DIOR_root + '/' + 'sabl_faster_rcnn_r50_fpn_2x.py'),
    gen_dict('DIOR_sabl_retina_full',
             DIOR_root + '/' + 'sabl_retinanet_r50_fpn_2x.py'),
    gen_dict('DIOR_res2net_full',
             DIOR_root + '/' + 'faster_rcnn_r2_101_fpn_2x.py'),
    gen_dict('DIOR_ssd_300_full',
             DIOR_root + '/' + 'ssd300.py'),
    gen_dict('DIOR_ssd_512_full',
             DIOR_root + '/' + 'ssd512.py'),
    gen_dict('DIOR_yolov3_d53_320_full',
             DIOR_root + '/' + 'yolov3_d53_320_273e_coco.py.py'),
    gen_dict('DIOR_yolov3_d53_mstrain-416_full',
             DIOR_root + '/' + 'yolov3_d53_mstrain-416_273e_coco.py'),
    gen_dict('DIOR_yolov3_d53_mstrain-608_full',
             DIOR_root + '/' + 'yolov3_d53_mstrain-608_273e_coco.py'),
    gen_dict('DIOR_libra_faster_rcnn_full',
             DIOR_root + '/' + 'libra_faster_rcnn_r50_fpn_2x.py'),
    gen_dict('DIOR_libra_retina_full',
             DIOR_root + '/' + 'libra_retinanet_r50_fpn_2x.py'),
    gen_dict('DIOR_pafpn_full',
             DIOR_root + '/' + 'faster_rcnn_r50_pafpn_2x.py'),
    gen_dict('DIOR_paa_full',
             DIOR_root + '/' + 'paa_r50_fpn_2x.py')
]
DIOR_voc_cfgs = {cfg.pop('name'):cfg for cfg in DIOR_voc_cfgs}