import argparse
import os
import sys

from .domHttpx import Domain
from domHttpx import config
from domHttpx.function import check_result, show_result, remove_result
from domHttpx.header import header as domhttpx_header
from domHttpx.write import info, error, tab

def parse_argument():
    usage = f"{os.path.basename(sys.executable)} {sys.argv[0]} [options]"
    parser = argparse.ArgumentParser(usage=usage)
    
    # Optional Options
    parser.add_argument('-v','--version', action='store_true', dest='version', help="Show version of domHttpx")
    parser.add_argument('-s','--silent', action='store_true', dest='silent', help='Silent mode (without banner and info)')
    parser.add_argument('-o', '--output', action='store', dest='output', help='File path to write output')
    parser.add_argument('-cr', '--check-result', action='store_true', dest='check_result', help='Check the result')
    parser.add_argument('-sr', '--show-result', action='store', dest='show_result', help='Show the result')
    parser.add_argument('-rr', '--remove-result', action='store', dest='remove_result', help='Remove result')
    # parser.add_argument('-cu', '--check-update', action='store_true', dest='check_update', help='Check domhttpx update')
    

    # Dorking Options
    dorking = parser.add_argument_group('DORKING')
    dorking.add_argument('-k','--keyword', action='store', dest='keyword', help="Search keyword/query")
    dorking.add_argument('-a','--amount', action='store', dest='amount', type=int, help="Specify result amount")
    
    # HTTX Options
    httpx = parser.add_argument_group('HTTPX')

    httpx.add_argument('-ip', '--only-ip', action='store_true', dest='ip', help='Shows IP')
    httpx.add_argument('-sc','--status-code', action='store_true', dest='status_code', help='Extracts status code')
    httpx.add_argument('-ws','--web-server', action='store_true', dest='server', help='Extracts server')
    httpx.add_argument('-t','--title', action='store_true', dest='title', help='Extracts title')
    httpx.add_argument('-p','--path', action='store', dest='path', help='Custom path')
    httpx.add_argument('-rp','--real-path', action='store_true', dest='real_path', help='Extracts path')
    httpx.add_argument('-od','--only-domain', action='store_true', dest='domain', help='Shows domain only')
    args = parser.parse_args()
    return args

def validation(args):
    if args.silent != True:
        domhttpx_header()

    if args.check_result == True:
        check_result()
        sys.exit()

    if args.show_result != None:
        show_result(args.show_result)
        sys.exit()

    if args.remove_result != None:
        remove_result(args.remove_result)
        sys.exit()

    if args.version:
        info('Now version is ' + config.version)
        sys.exit()

    if args.keyword == None:
        error('No input keyword detected')
        sys.exit()

    if args.amount == None:
        error('No input amount detected')
        sys.exit()


def main():
    args = parse_argument()
    init = Domain(args.keyword, args.amount)

    os.system('clear')
    
    validation(args)

    init.show()