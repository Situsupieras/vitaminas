---
name: video-production
description: "Standardized video production pipeline for TINITA HEALTH masterclasses and short-form content. Covers TTS audio generation, slide creation, video composition, and distribution. Use when producing educational videos, reels, or masterclass content for any product."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Video Production Pipeline

## Overview
Reusable pipeline for producing educational video content (Masterclasses, Reels, Shorts) for the 82 TINITA HEALTH products. Uses free tools (gTTS, Pillow, moviepy) with upgrade path to premium (HeyGen, ElevenLabs).

## When to Use
- Producing a Masterclass video (60 min) from a script
- Creating short-form video content (Reels/TikTok, 60s)
- Generating audio narration from text
- Creating branded slides/infographics
- Composing final video from assets

## The Presenter: Marco Villagrán
- **Role**: Especialista en Bienestar de TINITA HEALTH (NO usar "Dr." para evitar implicaciones médicas)
- **Appearance**: Latino, 38-42 años, barba corta, lentes, camisa gris oscuro mandarin collar
- **Voice**: `es-GT-AndresNeural` (Edge TTS) o gTTS español
- **Usage**: Same avatar for ALL 82 products (brand consistency)

## Production Pipeline

### Step 1: Script Cleanup
Convert markdown script to clean narration text:
```python
# Remove [Visual: ...] blocks, **bold**, speaker labels
python c:\proyectos\vitaminas\scratch\prepare_audio_text.py
```

### Step 2: Audio Generation
```powershell
# Option A: gTTS (Free, works everywhere)
.venv_marketing\Scripts\python scratch\generate_audio_gtts.py

# Option B: Edge TTS (Free, better quality, requires network)
edge-tts --voice es-GT-AndresNeural --file input.txt --write-media output.mp3

# Option C: ElevenLabs (Premium, $5/mo, best quality)
# Use ElevenLabs API with cloned voice
```

### Step 3: Slide Generation
```powershell
# Generate branded slides using Pillow
.venv_marketing\Scripts\python scratch\create_sample_slides.py
```

#### Brand Colors
| Element | Hex | Usage |
|:---|:---|:---|
| Background | `#1A1A2E` | Slide backgrounds |
| Primary Accent | `#16C79A` | Titles, highlights |
| Text Body | `#F5E6CA` | Body text |
| Alert/Danger | `#FF6B6B` | Myths, warnings |
| Logo | `#FFFFFF` | Lower right corner |

### Step 4: Video Composition
```powershell
# Compose: Avatar (left) + Slides (right) + Audio
.venv_marketing\Scripts\python scratch\compose_video.py
```

#### Layout Template
```
┌──────────────────────────────────────┐
│ ┌─────────┐ ┌──────────────────────┐ │
│ │ AVATAR  │ │      SLIDES          │ │
│ │  (1/3)  │ │       (2/3)          │ │
│ └─────────┘ └──────────────────────┘ │
│ [LOWER THIRD: Name + Title + Logo  ] │
└──────────────────────────────────────┘
Resolution: 1920x1080 @ 10fps (demo) / 24fps (production)
```

### Step 5: Distribution
- **YouTube**: Full masterclass (60 min)
- **Reels/TikTok**: Cut into 60s clips using hooks from `04_copy_assets.md`
- **Podcast**: Extract audio only (MP3)
- **Landing Page**: Embed on tiendasts.com/suplementos

## File Organization
```
{product_folder}/n8n_output/
├── 08_masterclass_script_60min.md    # Full script
├── 08_masterclass_section1_gtts.mp3  # Audio per section
├── 08_masterclass_section1_demo.mp4  # Video per section
└── assets/
    ├── slides/                        # Branded slides
    └── marco_villagran.png           # Presenter image
```

## Scaling to 82 Products
1. Generate script via n8n pipeline (Nodos 2-6)
2. Clean script → Audio → Slides → Compose (automated)
3. Same presenter, same colors, different product content
4. Estimated time per product: ~30 min (automated)

## Quality Gates
- [ ] Audio duration matches script length (~10 min per section)
- [ ] Slides follow brand color palette
- [ ] Avatar image is consistent across all videos
- [ ] Video resolution is 1920x1080
- [ ] Audio is clear and properly synced
- [ ] No watermarks or placeholder text in slides

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- gTTS voice quality is adequate for prototyping but not production-ready.
- Edge TTS requires internet connectivity and may fail on unstable networks.
- Lip-sync avatars (HeyGen) are NOT cost-effective at scale ($7,000+ for 82 products).
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
