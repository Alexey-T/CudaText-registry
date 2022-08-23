global T_LEXER,T_LINTER,T_FMT,T_TREE,T_INTEL,T_SNIP,T_OTHER,CLASSES,TYPE_TO_KIND,CLASSES_MSGS,REQS,PLUGINS

T_LEXER='[lexer]'
T_LINTER='[linter]'
T_FMT='[formatter]'
T_TREE='[tree helper]'
T_INTEL='[intel plugin]'
T_SNIP='[snippets]'
T_OTHER='[plugin]'

CLASSES=(
    T_LEXER,
    T_LINTER,
    T_FMT,
    T_TREE,
    T_INTEL,
    T_SNIP,
    T_OTHER,
    )

TYPE_TO_KIND = {
    T_LEXER: 'lexer',
    T_LINTER: 'linter',
    T_FMT: 'formatter',
    T_TREE: 'treehelper',
    T_INTEL: 'plugin',
    T_SNIP: 'snippets_ct',
    T_OTHER: 'plugin',
    }

CLASSES_MSGS={
    T_LEXER: 'Lexers:',
    T_LINTER: 'Linters:',
    T_FMT: 'Formatters:',
    T_TREE: 'Code Tree helpers:',
    T_INTEL: 'Code Intelligence plugins:',
    T_SNIP: 'Snippets:',
    T_OTHER: 'Other plugins:',
    }

REQS={
    T_LINTER: 'CudaLint',
    T_FMT: 'CudaFormatter',
    T_SNIP: 'Snippets',
}

PLUGINS={
    'Python':{
        T_LINTER:(
            'Python_using_pylint',
            'Python_using_pycodestyle',
            ),
        T_FMT:(
            'Python_Black',
            'Python_Fix_Imports',
            'Python_ReIndent',
            ),
        T_INTEL:(
            'Python_IntelliSense',
            ),
        T_SNIP:(
            'Python',
            ),
        T_OTHER:(
            'Configure_PyCodeStyle',
            'DevDocs',
            ),
        },
    'Lua':{
        T_LINTER:(
            'Lua_using_luac',
            ),
        T_FMT:(
            'Lua',
            ),
        T_SNIP:(
            'Lua',
            ),
        },
    'Pascal':{
        T_LEXER:(
            'Pascal',
            ),
        T_FMT:(
            'Embarcadero',
            ),
        T_SNIP:(
            'Pascal',
            ),
        T_TREE:(
            'Pascal',
            ),
        },
    'HTML/CSS':{
        T_LINTER:(
            'CSS_using_csslint',
            'CSS_using_csstree',
            'HTML_using_htmltidy',
            ),
        T_FMT:(
            'CSS_AutoPrefixer',
            'CSS_Comb',
            'CSS_Prefixer',
            'CSS_SASS_SCSS_LESS',
            'HTML_Beautify',
            'HTML_Soup',
            ),
        T_INTEL:(
            'Bootstrap_Completion',
            'HTML_Tidy',
            'HTML_Completion',
            ),
        T_TREE:(
            'HTML_XML',
            ),
        T_OTHER:(
            'HTML_Live_Preview',
            'HTML_Ops',
            'HTML_Tooltips',
            'CSS_CanIUse',
            'CSS_Property_Info',
            'CSS_Table_of_Contents',
            'Color_Picker',
            'DevDocs',
            'Font_Awesome',
            'FontStorage',
            ),
        T_SNIP:(
            'CSS_Grid',
            'CSS_Reset',
            'Atom-Sass',
            'FakeImg',
            'HTML_Handlebars',
            'Sublime-SCSS',
            ),
        T_LEXER:(
            'LESS',
            'Sass',
            'SCSS',
            'Stylus',
            'Svelte',
            'HTML_Diafan',
            'HTML_Django_DTL',
            'HTML_Embedded_JS',
            'HTML_Handlebars',
            'HTML_Laravel_Blade',
            'HTML_Liquid',
            'HTML_Mustache',
            'HTML_Smarty',
            ),
        },
    'JavaScript':{
        T_SNIP:(
            'Atom-JavaScript',
            'Atom-JavaScript-ES6',
            ),
        T_LINTER:(
            'CoffeeScript_using_coffee',
            'CoffeeScript_using_coffee-jshint',
            'CoffeeScript_using_coffeelint',
            'JavaScript_using_eslint',
            'JavaScript_using_jshint',
            'JavaScript_using_jsl',
            ),
        T_FMT:(
            'JavaScript_JSON',
            ),
        T_LEXER:(
            'CoffeeScript',
            'JavaScript_(ES6)',
            'JavaScript_(ES6)L',
            'JavaScript_Babel',
            'TypeScript',
            ),
        T_OTHER:(
            'JS_Multiline_Array',
            'DevDocs',
            'DocBlock_Comments',
            'Paste_as_String',
            ),
        T_INTEL:(
            'JS_Tern',
            ),
        },
    'PHP':{
        T_LINTER:(
            'PHP_using_phpcs',
            'PHP_using_phpl',
            'PHP_using_phplint',
            'PHP_using_phpmd',
            ),
        T_TREE:(
            'PHP',
            ),
        T_SNIP:(
            'PHP',
            ),
        T_OTHER:(
            'DevDocs',
            'DocBlock_Comments',
            ),
        },
    'SQL':{
        T_LEXER:(
            'MySQL_SQL',
            'MySQL_Stored_Procedures',
            'PL-SQL',
            'T-SQL',
            ),
        T_FMT:(
            'SQL_Parse',
            'SQL_Uroboro',
            ),
        T_OTHER:(
            'SQL_Tools',
            ),
        },
    'XML':{
        T_LINTER:(
            'XML_using_xmllint-libxml2',
            ),
        T_FMT:(
            'XML_IndentX',
            'XML_Pretty_Print',
            ),
        T_LEXER:(
            'XSLT',
            ),
        },
    'Go':{
        T_LEXER:(
            'Go',
            ),
        T_LINTER:(
            'Go_using_golint',
            'Go_using_gometalinter',
            'Go_using_gotype',
            'Go_using_go-vet',
            ),
        T_FMT:(
            'Go_gofmt',
            ),
        T_SNIP:(
            'Atom-Go',
            ),
        },
    'Markdown/reST/Textile/Wiki':{
        T_LEXER:(
            'R_Markdown',
            'Textile',
            'WikidPad',
            ),
        T_LINTER:(
            'Markdown_using_markdownlint',
            ),
        T_FMT:(
            'Markdown_Tables',
            ),
        T_TREE:(
            'MediaWiki',
            'reStructuredText',
            'Textile',
            'WikidPad',
            ),
        T_SNIP:(
            'Markdown',
            ),
        T_OTHER:(
            'Markdown_Editing',
            'Markdown_Preview',
            'Markdown_Special_Paste',
            'reStructuredText_Preview',
            'Textile_Preview',
            ),
        },
    'C/C++':{
        T_LINTER:(
            'C++_using_cppcheck',
            'C++_using_cpplint',
            'C++_using_gcc',
            ),
        T_FMT:(
            'AStyle',
            'Uncrustify',
            ),
        T_SNIP:(
            'Atom-C',
            'C_C++',
            ),
        T_OTHER:(
            'Paste_as_String',
            'Switch_Header',
            ),
        },
    'Ruby':{
        T_LEXER:(
            'HTML_Ruby-ERB',
            ),
        T_LINTER:(
            'Ruby_using_rubocop',
            'Ruby_using_ruby',
            ),
        T_FMT:(
            'Ruby',
            ),
        T_SNIP:(
            'Atom-Ruby',
            ),
        },
    '(General purpose)':{
        T_OTHER:(
            'Breadcrumbs',
            'Color_Picker',
            'Color_Text',
            'Colored_Indent',
            'Complete_From_Text',
            'Config_Toolbar',
            'CSV_Helper',
            'CudaExt',
            'Detect_Indent',
            'Differ',
            'Draw_Lines',
            'Encode',
            'External_Tools',
            'Favorites',
            'FindInFiles-v4',
            'FTP',
            'Hash_Generator',
            'Highlight_Occurrences',
            'Macros',
            'Numbered_Bookmarks',
            'Number_Utils',
            'Online_Search',
            'Open_URL',
            'Runner',
            'Session_Manager',
            'Show_Unicode_Name',
            'Snippets',
            'Spell_Checker',
            'Sync_Scroll',
            'Sync_Editing',
            'Tab_Icons',
            'Terminal_Plus',
            'Text_Statistics',
            ),
        },
    }
