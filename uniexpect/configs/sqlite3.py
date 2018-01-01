shell = {
    'command': 'sqlite3',
    'prompt': 'sqlite> ',
    'continuation': '>> ',
    'command_with_file': 'sqlite3 --init {filename}',
    '_load_file': '.read {filename}',  # 'command_with_file' takes precedence
}

language = 'sqlite3'
extension = 'sql'
block_comments = [('/*', '*/')]
inline_comments = ['--']

tests = [  # test formats higher up get precedence
    {
        'input_prefix': '>>> ',  # prefix for test input
        'output_prefix': '',  # prefix for test output
        'block_comments': True,  # like doctests, runs tests in block as a suite
        'inline_comments': False  # no output_prefix = no inline_comments
    },
    {
        'input_prefix': '-- >>> ',
        'output_prefix': '--',
        'block_comments': True,
        'inline_comments': False
    },
    {
        'input_prefix': '>',
        'output_prefix': '=>',
        'one-liner': True,
        'block_comments': True,
        'inline_comments': True
    }
]
