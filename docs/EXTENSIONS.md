# Extensions

## Markdown-to-Pelican

The main purpose of this project was to help me compile my Notion into 
Pelican-compliant markdown. This includes having a metadata section at the top
of the file.

This isn't _true_, portable markdown with this metadata. Hence I've decided to
keep it out of scope of this project. However it would be a nice extension to 
this project (potentially) where you can choose a compilation target and utilise
these additional features of each target.

But we can always have a markdown-to-pelican compiler anyway in the future.

## Notion JSON to Markdown

We have to make a lot of "guesses" and hacks to get the Notion markdown to work
exactly as we expect. We might have a better time of it all if we instead use
the **JSON** information of Notion pages.

This JSON document is much better structured and means we don't really need to
do any parsing of the original markdown but, instead, can just focus on compiling
the JSON into a more concise markdown format.