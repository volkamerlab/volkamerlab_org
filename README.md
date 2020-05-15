# volkamerlab.org

Contents for this website, built with Hugo, a static site generator, and deployed to netlify.com.

This website is based on the [HTML5 Editorial](https://html5up.net/editorial) template.

## Request changes

1. Fork and create a branch on your fork.
2. Install `hugo` from package file on GitHub ([v0.65.3](https://github.com/gohugoio/hugo/releases/tag/v0.65.3)).
   - Ubuntu: `hugo_extended_0.65.3_Linux-64bit.deb`
   - Windows: `hugo_extended_0.65.3_Windows-64bit.zip`
   - macOS: `hugo_extended_0.65.3_macOS-64bit.tar.gz`
3. Run `hugo serve` on this directory while editing. It will autoreload changes on `localhost:1313`.
4. Add, commit, push and submit PR. Netlify will create a deploy preview for you on the PR.
5. Wait for review.

## Add new content

Use `hugo new`! This will autopopulate some fields for you (e.g. date). You need to specify the path to the new document, like:

```
hugo new projects/my_new_project.md
```

Notice how the path is relative to `/content`. Hugo will guess that you are creating a new page of type `project` (because of the parent folder), and use the corresponding template in `/archetypes`.

## Insert a page inside another

You can use _shortcodes_ along your normal markdown for this. Path is relative to `/content`. Notice the `{{% %}}` syntax!

```
{{% content "path/to/page/to/be/inserted.md" %}}
```

## Available shortcodes

In addition to the [default shortcodes](https://gohugo.io/content-management/shortcodes/), we provide:

* `{{< xfigure ... >}}`: derived from [`figure`](https://gohugo.io/content-management/shortcodes/#figure), but using the theme image wrappers for responsiveness. Also accepts an `imageclass` attribute to define [custom fittings](https://html5up.net/uploads/demos/editorial/elements.html): `fit`, `left`, `right`.
* `{{% content ... %}}`: insert a markdown content in another article.
* `{{% person ... %}}`: link to a person profile using their person key (check `/data/team/members.yaml`).

## Project pages vs Research pages

Every project is described at `/content/projects/project_name.md`. The frontmatter define most of the metadata you need. The markdown content after the frontmatter is free text and can be considered the "abstract" of the project.

Research pages live at `/content/research/research_line.md`. They provide overviews of the different research fields of the group, and can embed _project pages_ thanks to the `{{% content %}}` shortcode. The `content` shortcode will only embed the Markdown text, though! It does provide a link to the project page for more information.


## Where to look for modifications

### Menu

- __Welcome__: `content/_index.md`
- __Research__: `content/research/_index.md/`. Subitems in the menu are in the corresponding `*.md` files.
- __The team__: `content/team/_index.md` (intro text) + `data/team/members.yaml` (member info). Almost everything is encoded in the YAML file. Adding more members is a matter of editing the lists. Responsible code for orchestrating the layout is in `layouts/section/team.html`; each individual member is rendered through `layouts/partials/person.html`.
- __Publications__: `content/publications/_index.md` (intro text) + `data/publications/publications.yaml` (database). Read the comments at the top of the YAML file for more info.

### Get in touch

Hardcoded in `partials/contact.html`

### Copyright

Hardcoded in `partials/sidebar_footer.html`

### Header bar

Where the social icons are listed on the right. This part is hardcoded in `partials/topbar.html`.


## Adding pages to the menu

After creating a new `*.md` file in `content/`, you can add it to the menu by specifying this metadata in the YAML header:

```
menu: "main"
```

If the default ordering is not suitable, it can be overriden with a weight:

```
weight: 10
```

Nested submenus must specify the parent too:

```
menu:
    main:
        parent: Research
```

## Resources

### Content management

* HTML5 Editorial [sample content](https://html5up.net/uploads/demos/editorial/elements.html): Check out content options.
* Hugo [shortcodes](https://gohugo.io/content-management/shortcodes/): Use shortcodes instead of HTML in markdown content. We can create more if needed (check `/layouts/shortcodes`), so let us know if you need something extra.


## FAQ

* You added a new markdown content file `/content/folder/file.md` but the file content does not show up on the website's menu or a section?
    * Check if the `publishdate` in your file is in the future. If so, you will only be able to see the page when rendering the website using `hugo serve -F`.
    * Check if `draft: true`. If that's the case, these will only be rendered with `hugo serve -D`. Remember to set `draft: false` when the content is ready to be published (or remove that line entirely).
