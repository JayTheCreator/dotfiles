syntax on

set encoding=UTF-8
set number
set ruler
set relativenumber
set nobackup
set noswapfile

call plug#begin()
Plug 'preservim/nerdtree'
Plug 'OmniSharp/omnisharp-vim'
call plug#end()

nmap <C-n> :NERDTreeToggle<CR>
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
