# CelebV-Text: A Large-Scale Facial Text-Video Dataset

<img src="./assets/teaser.png" width="96%" height="96%">


**CelebV-HQ: A Large-Scale Video Facial Attributes Dataset**<br>
[Jianhui Yu](https://scholar.google.com/citations?user=sdxlMmMAAAAJ&hl=en)\*,
[Hao Zhu](https://www.zhuhaozh.xyz)\*,
[Liming Jiang](https://liming-jiang.com/),
[Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/),
[Weidong Cai](https://weidong-tom-cai.github.io/),
and [Wayne Wu](https://wywu.github.io/),
<br>
(*Equal contribution)</small><br>
**[Demo Video]()** | **[Project Page](https://celebv-text.github.io/)**
| **[Paper]()**
| **[Annotations](https://github.com/celebv-text/CelebV-Text/blob/main/celebvtext_info.json)**

> Currently, text-driven generation models are booming in video editing with their compelling
> results.
> However, for the face-centric text-to-video generation, challenges remain severe as a suitable
> dataset with high-quality videos and highly-relevant texts is lacking.
> In this work, we present a large-scale, high-quality, and diverse facial text-video dataset, <b>CelebV-Text</b>,
> to facilitate the research of facial text-to-video generation tasks.
> CelebV-Text contains 70,000 in-the-wild face video clips covering diverse visual content.
> Each video clip is paired with 20 texts generated by the proposed semi-auto text generation
> strategy,
> which is able to describe both the static and dynamic attributes precisely.
> We make comprehensive statistical analysis on videos, texts, and text-video relevance of
> CelebV-Text,
> verifying its superiority over other datasets.
> Also, we conduct extensive self-evaluations to show the effectiveness and potential of
> CelebV-Text.
> Furthermore, a benchmark is constructed with representative methods to standardize the
> evaluation of the facial text-to-video generation task.

## Updates

- [28/12/2022]
    - The codebase and project page are created.
    - The download and processing tools for the dataset is released. Use them to construct your CelebV-Text!

## TODO

- [x] Data download and processing tools.
- [ ] Data annotations.
- [ ] Inference code of unconditional video generation
- [ ] Pretrained models of unconditional video generation

## Statistics


https://user-images.githubusercontent.com/121470971/209757073-77fd707b-e8cc-49ea-8d1d-836bc43d078f.mp4


The distributions of each attribute. CelebV-Text contains <b>70,000 video clips</b> with a total duration of around <b>
279 hours</b>.
Each video is accompanied by <b>20 sentences</b> describing <b>6 designed attributes</b>,
including 40 general appearances, 5 detailed appearances, 6 light conditions, 37 actions, 8 emotions, and 6 light directions.

<img src="./assets/video_stats.png" width="96%" height="96%" alt="video stats">
<img src="./assets/text_stats.png" width="96%" height="96%" alt="text stats">
<img src="./assets/text_video_rel.png" width="96%" height="96%" alt="text-video rel">

## Agreement

- The CelebV-Text dataset is available for non-commercial research purposes only.
- All videos of the CelebV-Text dataset are obtained from the Internet which are not property of our institutions. Our
  institutions are not responsible for the content nor the meaning of these videos.
- You agree not to reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purposes, any portion
  of the videos and any portion of derived data.
- You agree not to further copy, publish or distribute any portion of the CelebV-Text dataset. Except, for internal use at
  a single site within the same organization it is allowed to make copies of the dataset.

## Download

### Text Descriptions
| Description                         |                                                    Link                                                     |
|:------------------------------------|:-----------------------------------------------------------------------------------------------------------:| 
| general & detailed face attributes  |     [Google Drive](https://drive.google.com/file/d/1WBLf0t9EOsuPWmsU4qnFuv_w2dobd-xT/view?usp=sharing)      |
| emotion                             |     [Google Drive](https://drive.google.com/file/d/18V-72aa36r3ZTmu2NHZIMM8aW-0PdKC-/view?usp=sharing)      |
| action                              |     [Google Drive](https://drive.google.com/file/d/1N6Xf2GGstyj--taKnRi5gBd-pXAQX3cI/view?usp=sharing)      | 
| light direction                     |     [Google Drive](https://drive.google.com/file/d/1RwBEBse8Y5aseE7jC4Gu2R177YnpAB8g/view?usp=sharing)      |
| light intensity                     |     [Google Drive](https://drive.google.com/file/d/1o5w2KkXjZi2wygM5z-nL6tWtGGFLcHHO/view?usp=sharing)      |
| light color temperature             |     [Google Drive](https://drive.google.com/file/d/15bcEu6xUtoPZk6kCeYQc01JbKnlt8BFR/view?usp=sharing)      |

[//]: # (### TL;DR:)

[//]: # ()
[//]: # (This **[issue]&#40;https://github.com/CelebV-HQ/CelebV-HQ/issues/8&#41;** is helpful.)

### Usage:

Prepare the environment:

```bash
pip install youtube_dl
pip install opencv-python
```

Run script:

```bash
# you can change the download folder in the code 
python download_and_process.py
``` 

### JSON File Structure:

```javascript
{
    "clips":
    {
        "0-5BrmyFsYM_0":  // clip 1 
        {
            "ytb_id": "0-5BrmyFsYM",                                        // youtube id
            "duration": {"start_sec": 0.0, "end_sec": 9.64},                // start and end times in the original video
            "bbox": {"top": 0, "bottom": 937, "left": 849, "right": 1872},  // bounding box
            "version": "v0.1"
        },
      
        "00-30GQl0TM_7":  // clip 2 
        {
            "ytb_id": "00-30GQl0TM",                                        // youtube id
            "duration": {"start_frame": 415.29, "end_frame": 420.88},       // start and end times in the original video
            "bbox": {"top": 0, "bottom": 1183, "left": 665, "right": 1956}, // bounding box
            "version": "v0.1"
        },
        "..."
        "..."

    }
}
```

## Baselines

### Facial Text-to-Video Generation

To train the baselines, we used their original implementations in our paper:

- [MMVID](https://github.com/snap-research/MMVID)
- [TFGAN](https://github.com/minrq/CGAN_Text2Video)


[//]: # (## Related Works)

[//]: # ()
[//]: # (* &#40;ECCV 2022&#41; **StyleGAN-Human: A Data-Centric Odyssey of Human Generation**, Jianglin Fu et)

[//]: # (  al. [[Paper]&#40;https://arxiv.org/pdf/2204.11823.pdf&#41;], [[Project Page]&#40;https://stylegan-human.github.io/&#41;])

[//]: # (  , [[Dataset]&#40;https://github.com/stylegan-human/StyleGAN-Human&#41;])

## Citation

If you find this work useful for your research, please consider citing our paper:

[//]: # (```bibtex)

[//]: # (@inproceedings{zhu2022celebvhq,)

[//]: # (  title={{CelebV-HQ}: A Large-Scale Video Facial Attributes Dataset},)

[//]: # (  author={Zhu, Hao and Wu, Wayne and Zhu, Wentao and Jiang, Liming and Tang, Siwei and Zhang, Li and Liu, Ziwei and Loy, Chen Change},)

[//]: # (  booktitle={ECCV},)

[//]: # (  year={2022})

[//]: # (})

[//]: # (```)

## Acknowledgement

[//]: # (This work is partly supported by Shanghai AI Laboratory and SenseTime Research. It is also supported by NTU NAP, MOE AcRF Tier 1 &#40;)

[//]: # (2021-T1-001-088&#41;, and under the RIE2020 Industry Alignment Fund – Industry Collaboration Projects &#40;IAF-ICP&#41; Funding)

[//]: # (Initiative, as well as cash and in-kind contribution from the industry partner&#40;s&#41;.)
