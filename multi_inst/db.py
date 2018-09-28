global T_LEXER,T_LINTER,T_TREE,T_INTEL,T_SNIP,T_OTHER,CLASSES,TYPE_TO_KIND,CLASSES_MSGS,PLUGINS

T_LEXER='[lexer]'
T_LINTER='[linter]'
T_TREE='[tree helper]'
T_INTEL='[intel plugin]'
T_SNIP='[snippets]'
T_OTHER='[plugin]'

CLASSES=(
    T_LEXER,
    T_LINTER,
    T_TREE,
    T_INTEL,
    T_SNIP,
    T_OTHER,
    )
    
TYPE_TO_KIND = {
    T_LEXER: 'lexer',
    T_LINTER: 'linter',
    T_TREE: 'treehelper',
    T_INTEL: 'plugin',
    T_SNIP: 'snippets',
    T_OTHER: 'plugin',
    }

CLASSES_MSGS={
    T_LEXER: 'Lexers:',
    T_LINTER: 'Linters:',
    T_TREE: 'Code Tree helpers:',
    T_INTEL: 'Code Intelligence plugins:',
    T_SNIP: 'Snippets:',
    T_OTHER: 'Other plugins:',
    }

PLUGINS={
    'Python':{
        T_LINTER:(
            'Python_using_pylint',
            'Python_using_pep8',
            ),
        T_INTEL:(
            'Python_Intel',
            ),
        T_SNIP:(
            'Python',
            ),
        T_OTHER:(
            'Python_Fix_Imports',
            'Configure_PEP8',
            'DevDocs',
            ),
        },
    'Lua':{
        T_LINTER:( 
            'Lua_using_luac', 
            ),
        T_SNIP:( 
            'Lua',
            ),
        T_OTHER:(
            'Lua_Format',
            ),
        },
    'Pascal':{
        T_SNIP:(
            'Pascal',
            ),
        T_TREE:(
            'Pascal',
            ),
        T_OTHER:(
            'Pascal_C++_Format',
            ),
        },
    'HTML/CSS':{
        T_LINTER:(
            'CSS_using_csslint',
            'CSS_using_csstree',
            'HTML_using_htmltidy',
            ),
        T_INTEL:(
            'HTML_Tidy',
            'HTML_Completion',
            ),
        T_OTHER:(
            'HTML_Beautify',
            'HTML_Ops',
            'HTML_Tooltips',
            'CSS_AutoPrefixer',
            'CSS_CanIUse',
            'CSS_Comb',
            'CSS_Format',
            'CSS_Minifier',
            'CSS_Prefixer',
            'CSS_Table_of_Contents',
            'Color_Picker',
            'DevDocs',
            'Emmet_Lite',
            'Font_Awesome',
            'Web_Font',
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
            'JavaScript_using_eslint',
            'JavaScript_using_jshint',
            'JavaScript_using_jsl',
            ),
        T_LEXER:(
            'JavaScript_Babel',
            'TypeScript',
            'CoffeeScript',
            ),
        T_OTHER:(
            'JS_Format',
            'JS_Minifier',
            'JS_Multiline_Array',
            'JS_Sort_Imports',        
            'DevDocs',
            'DocBlock_Comments',
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
            'PL_SQL',
            'SQL_Blue',
            'SQL_White',
            'T-SQL',
            ),
        T_OTHER:(
            'SQL_Format',
            'SQL_Tools',
            'Uroboro_SQL_Format',
            ),
        },
    'XML':{
        T_LINTER:(
            'XML_using_xmllint-libxml2',
            ),
        T_OTHER:(
            'XML_Format',
            'XML_Tidy',        
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
            'Go_using_gotype',
            'Go_using_go-vet',
            ),
        T_SNIP:(
            'Atom-Go',
            ),
        },
    }
    
