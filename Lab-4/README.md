# Lab 4: VibeCoding (Q*bert Repair)

**Student:** Pranav &bull; **SRN:** PES1UG24CS466  
**Assigned repo:** [SETAPESU26/35_qbert](https://github.com/SETAPESU26/35_qbert)  
**AI tool used:** Claude Code

## Deliverables

| Deliverable | File |
| --- | --- |
| Video before changes | [before_video.mp4](before_video.mp4) |
| Video after changes | [after_video.mp4](after_video.mp4) |
| Updated code | [35_qbert/game.py](35_qbert/game.py) |
| Chat history | [Lab_4_Chat_History.pdf](Lab_4_Chat_History.pdf) |

## What changed in `game.py`

| Task | Change |
| --- | --- |
| 1. Projection bug | `cube_center` used `row // 2`, which rounds odd rows and skews the pyramid. It now uses `row / 2`. |
| 2. `cube_palette(level)` | Returns one of four 3-colour palettes, repeating after level 4. Level 1 keeps the default colours. |
| 3. `on_cube_completed(cell)` | Starts a 0.35s white flash on the cube that was just completed. |
| 4. `bonus_life_threshold()` | Returns `1000`, so a life is awarded at every 1000 points. |

The flash also needed small changes outside the hook: `flashes.clear()` in `Game.reset`, a countdown at the top of `Game.update`, and a colour blend in `Game.draw_cube`. The countdown runs before the state check so the last cube's flash still fades on the level-clear screen.

## What the videos show

Both videos are 10 seconds long. They were captured by a script that ran the real `game.py` and saved its frames, with a simple bot pressing the keys instead of a person.

- **Before:** the original code, with rows drifting sideways so the pyramid is skewed.
- **After:** the symmetric pyramid and cube flashes, a bonus life at 1000 points (1.2s), the level clear (7.7s), the level 2 palette (8.5s), and a second bonus life at 2000 points (9.6s). This clip is a continuous 10-second part of a longer run.

## Run it

```bash
pip install pygame
python 35_qbert/game.py
```

**Controls:** arrow keys to hop diagonally, `R` to reset, Space to continue after clearing a level.
