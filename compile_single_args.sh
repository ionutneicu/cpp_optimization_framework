#!/bin/sh

#ARGS="-fdefer-pop -fmerge-constants -fthread-jumps -floop-optimize -fcrossjumping -fif-conversion -fif-conversion2 -fdelayed-branch -fguess-branch-probability -fcprop-registers -foptimize-sibling-calls -fstrength-reduce -fcse-follow-jumps  -fcse-skip-blocks -frerun-cse-after-loop  -frerun-loop-opt -fgcse   -fgcse-lm   -fgcse-sm -fdelete-null-pointer-checks -fexpensive-optimizations -fregmove -fschedule-insns  -fschedule-insns2 -fsched-interblock  -fsched-spec -fcaller-saves -fpeephole2 -freorder-blocks  -freorder-functions -fstrict-aliasing -falign-functions  -falign-jumps -falign-loops  -falign-labels"

ARGS="-fbranch-count-reg -fcombine-stack-adjustments -fcompare-elim -fcprop-registers -fdefer-pop -fforward-propagate -fguess-branch-probability -fif-conversion -fif-conversion2 -finline-functions-called-once -fipa-profile -fipa-pure-const -fipa-reference -fipa-reference-addressable -fmove-loop-invariants -fomit-frame-pointer -freorder-blocks -fshrink-wrap -fsplit-wide-types -fssa-phiopt -ftree-bit-ccp -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars -ftree-copy-prop -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-fre -ftree-pta -ftree-sink -ftree-slsr -ftree-sra -ftree-ter"
SRC="optimization_check.cpp"

g++ ${ARGS} ${SRC} -o runopt -lpthread
