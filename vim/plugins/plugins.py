from talon import Context, Module, actions, app, settings, ui

mod = Module()

# talon vim plugins. see vim/plugins/
# to enable plugins you'll want to set these inside the corresponding mode
# talon file.
# XXX - that should just be automatically done based off the file names inside
# of the plugin folder since it's annoying to manage
# TODO: It would be good to mark some of these with nvim if their specific to neovim
plugin_tag_list = [
    "vim_ale",
    "vim_change_inside_surroundings",
    "vim_codeql",
    "vim_comment_nvim",
    "vim_copilot",
    "vim_cscope",
    "vim_easy_align",
    "vim_easymotion",
    "vim_eunuch",
    "vim_fern",
    "vim_fern_mapping_fzf",
    "vim_floaterm",
    "vim_fugitive",
    "vim_fugitive_summary",
    "vim_fzf",
    "vim_grammarous",
    "vim_lightspeed",
    "vim_leap",
    "vim_lsp",
    "vim_markdown",
    "vim_markdown_preview",
    "vim_markdown_toc",
    "vim_mason",
    "vim_mkdx",
    "vim_null_ls",
    "vim_follows_md_links",
    "vim_lazy",
    "vim_nerdtree",
    "vim_obsession",
    "vim_plug",
    "vim_rooter",
    "vim_signature",
    "vim_suda",
    "vim_surround",
    "vim_taboo",
    "vim_tabular",
    "vim_taskwiki",
    "vim_telescope",
    "vim_test",
    "vim_treesitter",
    "vim_treesitter_textobjects",
    "vim_unicode",
    "vim_ultisnips",
    "vim_wiki",
    "vim_you_are_here",
    "vim_youcompleteme",
    "vim_zenmode",
    "vim_zoom",
    "vim_trouble",
    "vim_luasnip",
    "vim_nvim_cmp",
    "vim_flip_ext",
]
for entry in plugin_tag_list:
    mod.tag(entry, f"tag to load {entry} vim plugin commands")

# TODO: rename tag to vim_plugins?
mod.tag("vim", desc="a tag to load various vim plugins")
