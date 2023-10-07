# Meander for Sublime Text

[Meander](https://github.com/qxoko/meander) is a production writing utility for rendering and analysing screenplays.  While you don't have to have Meander installed to use this package, it's recommended to use them in tandem for the full benefit.

Meander for Sublime Text provides a simple, customisable and distraction-free experience out of the box for Fountain writing, a semantically-compatible Fountain syntax definition for use with Meander, as well as number of quality of life features, like an in-text scene number generator and navigation tools tailored to screenplays.

This package is also intended as a reference implementation for how screenwriting with Meander should be supported and facilitated in other text editors.

This document will make reference to Fountain syntax and Meander features without necessarily explaining them in depth.  If you're unfamiliar with Fountain, please read about [Fountain](https://fountain.io/syntax) and [Meander](https://github.com/qxoko/meander) first.

## Table of Contents

<!-- MarkdownTOC autolink="true" -->

- [Commands](#commands)
	- [Move to Section](#move-to-section)
	- [Move to Note Tag](#move-to-note-tag)
	- [Open Included Files](#open-included-files)
	- [Add Scene Numbers](#add-scene-numbers)
	- [Remove Scene Numbers](#remove-scene-numbers)
	- [Toggle Boneyards](#toggle-boneyards)
- [Project Files](#project-files)
- [Syntax](#syntax)
	- [Scope List](#scope-list)
- [Recommended Packages / Tweaks](#recommended-packages--tweaks)
	- [Theme Colours](#theme-colours)

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
			"forward": false,
			"include_scenes": true,
		}
	},
	{
		"keys": ["f10"],
		"command": "meander_move_to_section",
		"args": {
			"forward": true,
			"include_scenes": true,
		}
	}
]
```

The `include_scenes` argument will optionally add scene headings as navigable targets, but is disabled by default.

This scene switch allows the same command to be useful for both screenwriters with their Scene Headings and authors using Meander's manuscript mode, where Sections are used as chapter headings.

### Move to Note Tag

Sublime Command: `meander_move_to_note_tag`

A note tag is a word, prefixed with an `@` symbol inside a Note or Boneyard, such as `@todo` or `@fixthis`.  They are not recognised by Fountain or Meander and are only present in this syntax package as a helpful visual aide to help important reminders stand out:

```fountain
[[@todo this whole passage is lacking clarity]]
```

This command adds forward/backward navigation between these tags, facilitating quick navigation between all the items in your writing to-do list:

```json
[
	{
		"keys": ["f9"],
		"command": "meander_move_to_tag",
		"args": {
			"forward": false,
		}
	},
	{
		"keys": ["f10"],
		"command": "meander_move_to_tag",
		"args": {
			"forward": true,
		}
	}
]
```

### Open Included Files

Sublime Command: `meander_open_include`

"Open Include" is a drop-in replacement for Sublime's "Goto Definition" that allows the user to open the file path of an `include` with a shortcut.

This is *enabled* by default within the package using F12, which idiomatically replaces the default "Goto Definition" shortcut when used within a Fountain file.

### Add Scene Numbers

Sublime Command: `meander_add_scene_numbers`

Adds `#1#` formatted scene numbers to every scene heading, **replacing any existing ones**.  This only provides integer numbering and does not cross over included files; it operates on the active buffer only.

This is obviously a feature better provided by Meander itself, but in the event that you want to bake scene numbers directly into the text, such as for an archival copy, you might use Meander's text merge to produce a monolithic file and then this command to write in the plain text scene numbers.

### Remove Scene Numbers

Sublime Command: `meander_remove_scene_numbers`

Strips out any `#1#` scene numbers from the current file.  The removal command will catch any valid scene numbers, such as `#1#`, `#1-A#`, `#1.A-A#`.

### Toggle Boneyards

Sublime Command: `meander_toggle_boneyard`

Toggles (by folding) all `/* boneyard */` regions in the current file, useful for visually simplifying an in-progress document dense with notes and reminders.

## Project Files

When setting up a writing workspace with Sublime, it may be sensible to set up a custom build.  This package comes with a build system featuring a few simple presets for Meander, but you may want to set up specific flags for a particular project so you don't have to use the terminal every time.

Here's an example of a `.sublime-project` file with a custom build for Meander that generates scene numbers, but preserves `[[notes]]` in the output:

```json
{
	"folders":
	[
		{
			"path": ".",
			"file_exclude_patterns": ["*.sublime-project"]
		}
	],
	"build_systems": [
		{
			"name": "Custom Meander",
			"working_dir": "$project_path",
			"cmd": ["meander", "$file", "--notes", "-s", "generate"]
		}
	]
}
```

## Syntax

The included syntax definition for Fountain, in addition to the base syntax, supports the additional extensions Meander has either provided or supported from other Fountain editors.

The scope names are carefully selected to match other markup languages and use Sublime's own [Scope Naming](https://www.sublimetext.com/docs/scope_naming.html) recommendations where possible to ensure most themes will look sensible out of the box.

### Scope List

| Fountain Syntax  | Scope |
|------------------|-------|
| Scene headings | `entity.name.section` |
| Scene numbers | `entity.name.enum` |
| Section headings | `punctuation.definition.heading` |
| `header`/`footer` | `keyword.control` |
| `include` | `keyword.control.import` |
| Title Page | `variable.language` |
| Title Values | `string.unquoted` |
| Character Names | `string` |
| Force Characters (`@`, `!`, etc.) | `constant.other` |
| Bold | `markup.bold` |
| Italics | `markup.italic` |
| Underline | `markup.underline` |
| Highlight | `markup.quote` |
| Synopses | `comment.line` |
| Note Markers | `punctuation.definition.comment` |
| Notes | `comment` |
| Counters | `variable.control.fountain` |
| Boneyard Markers | `punctuation.definition.comment` |
| Boneyard Content | `comment.block` |
| Boneyard Tags (`@todo`, etc.) | `variable.annotation` |

## Recommended Packages / Tweaks

In addition to the Meander package, I recommend the following packages for a minimal, distractionless Sublime writing experience:

- The [Alabaster Theme](https://github.com/tonsky/sublime-scheme-alabaster) for an extremely clean light-mode that works very well with Fountain.
- The [Typewriter](https://github.com/alehandrof/Typewriter) package, which provides a typewriter-scroll mode that locks the scrolling position to the caret as you type.

### Theme Colours

Using the parent Fountain scope `text.fountain`, specific theme tweaks can be made for better customisation.

Here's one I use personally, which inverts scene headings (and scene numbers) to make them extremely visible:

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