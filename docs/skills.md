---
hide:
  - navigation
---
# Agent skills


The `dyscolab-modeling` [agent skill](https://agentskills.io) teaches coding agents (Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and others) how to model systems using [Poincare](poincare.md), [SimBio](simbio.md) and [Jablonski](jablonski.md). With the skill installed, an agent can declare, simulate and analyse models following the libraries' conventions, instead of guessing the API. It uses the open `SKILL.md` format, so it works with any agent that supports Agent Skills.

---
## Installation

### Bundled with the libraries (recommended)

Poincare, SimBio and Jablonski ship the skill and install it into the environment, at `<environment>/share/agent-skills/dyscolab-modeling/`. This copy always matches the installed library versions (Poincare 1.3.0 and newer).

**pixi projects:** link it into your agent's skills folder with [pixi skills](https://pixi.prefix.dev/dev/integration/extensions/pixi_skills/). The link follows the environment, so the skill updates together with the libraries:

```sh
pixi global install pixi-skills                   # once
pixi skills manage --backend claude --scope local  # or another agent's backend
```

**Any environment:** copy it with the environment's Python. Run the same command again after upgrading or adding a library:

```sh
python -m poincare.skill install --dest .agents/skills   # or .claude/skills, ~/.codex/skills, ...
python -m poincare.skill check .agents/skills/dyscolab-modeling
```

### From the skills repository

This copy documents the library releases listed in its `SKILL.md`, and doesn't follow the versions installed in your environment.

**Any agent**, with the [skills CLI](https://skills.sh):

```sh
npx skills add dyscolab/skills
```

**Claude Code**, as a plugin marketplace:

```sh
claude plugin marketplace add dyscolab/skills
claude plugin install dyscolab@dyscolab
```

**Manually:** copy the `skills/dyscolab-modeling/` folder of the repository into your agent's skills directory (for example `.agents/skills/`, `.claude/skills/` or `~/.codex/skills/`).

---
## Usage

Once installed, there is nothing else to configure: the agent loads the skill on its own when you ask it to model kinetics, reaction networks, ODEs or photophysical systems, or when you mention Poincare, SimBio or Jablonski. In agents that support it, you can also invoke it explicitly (in Claude Code, `/dyscolab-modeling`).

--- 
## Github
The skill's source can be found in the [dyscolab/skills](https://github.com/dyscolab/skills) repository.