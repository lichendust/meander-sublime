# Meander for Sublime Text

[Meander](https://github.com/qxoko/meander) is a production writing utility for rendering and analysing screenplays.  While you don't have to have Meander installed to use this plugin, it's recommended to use them in tandem for the full benefit.

This plugin offers a semantically-compatible Fountain syntax definition for use with Meander, as well as number of quality of life features, like an in-text scene number generator and navigation tools tailored to screenplays.

It also provides a simple, customisable and distraction-free experience out of the box for Fountain writing.

Meander for Sublime Text is also intended as a reference implementation for how screenwriting with Meander should be supported and facilitated in other text editors.

## Table of Contents

<!-- MarkdownTOC autolink="true" -->

- [Commands](#commands)
	- [Move to Section](#move-to-section)
	- [Open Included Files](#open-included-files)
	- [Add Scene Numbers](#add-scene-numbers)
	- [Remove Scene Numbers](#remove-scene-numbers)
	- [Toggle Boneyards](#toggle-boneyards)
- [Syntax](#syntax)
- [Planned/Experimental Features](#plannedexperimental-features)

<!-- /MarkdownTOC -->

## Commands

### Move to Section

Sublime Command: `meander_move_to_section`

Move to section adds forward/backward navigation between Scene Headings and Sections, facilitating quick navigation around a screenplay.  It mirrors the conventions of other `move_to` commands in Sublime:

```json
[
	{
		"keys": ["f9"],
		"command": "meander_move_to_section",
		"args": {
			"forward": false
		}
	},
	{
		"keys": ["f10"],
		"command": "meander_move_to_section"
	}
]
```

(Due to this plugin's careful selection of scope names, this feature also works on Markdown files.)

### Open Included Files

Sublime Command: `meander_open_include`

"Open Include" is a drop-in replacement for Sublime's "Goto Definition" that allows the user to open the file path of an `{{include}}` from its reference in the text.

This is enabled by default within the package, using `F12`, which idiomatically replaces the default "Goto Definition" shortcut.

### Add Scene Numbers

Sublime Command: `meander_add_scene_numbers`

Adds `#1#` formatted scene numbers to every scene heading, *replacing any existing ones*.  This only provides integer numbering and does not cross over included files.

### Remove Scene Numbers

Sublime Command: `meander_remove_scene_numbers`

Strips out any `#1#` scene numbers from the current file.  The removal command (and syntax highlighting) will catch any valid scene numbers, such as `#1#`, `#1-A#`, `#1.A-A#`.

### Toggle Boneyards

Sublime Command: `meander_toggle_boneyard`

Hides or reveals (by folding) all `/* boneyard */` regions in the current file, useful for visually simplifying an in-progress document dense with notes and reminders.

## Syntax

The included syntax definition for Fountain, supports the additional syntax extensions Meander has either provided or supported from other Fountain editors.

The scope names are carefully selected to match other markup languages and use Sublime's own [Scope Naming] recommendations where possible to ensure most themes will look sensible out of the box.

The entire Fountain scope is defined under `text.fountain`, allowing savvy users to make specific tweaks to their themes for better support.  Here's one I use personally, which inverts scene headings (and scene numbers) to make them extremely visible:

```json
{
	"scope": "text.fountain entity.name.section",
	"foreground": "black",
	"background": "white",
	"selection_foreground": "white",
},
{
	"scope": "text.fountain entity.name.enum",
	"foreground": "black",
	"background": "purple",
	"selection_foreground": "white",
},
```

(Adjust colours to taste or to your theme).

## Planned/Experimental Features

+ Supporting a version of "Go to Definition/Scope" for the `{{include}}` syntax, allowing Sublime to open included files from within the text.