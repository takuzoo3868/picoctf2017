<!-- This markdown file is writeup template. -->

## Yarn 55pt

### Problem
> I was told to use the linux strings command on [yarn](https://webshell2017.picoctf.com/static/9adb6ebf01d8755201564dba69bc1a92/yarn), but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back

### Answer
Let's see the binary...

```bash
$ strings yarn 
/lib/ld-linux.so.2
U^TR
libc.so.6
_IO_stdin_used
putchar
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh 
[^_]
;*2$"(
GCC: (Debian 4.9.2-10) 4.9.2
GCC: (Debian 4.8.4-1) 4.8.4
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
crtstuff.c
__JCR_LIST__
deregister_tm_clones
register_tm_clones
__do_global_dtors_aux
completed.6279
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
yarn.c
__FRAME_END__
__JCR_END__
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
__x86.get_pc_thunk.bx
data_start
_edata
_fini
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
putchar@@GLIBC_2.0
_end
_start
_fp_hw
__bss_start
main
_Jv_RegisterClasses
__TMC_END__
_ITM_registerTMCloneTable
_init

```

I didn't find flag message. So, specify the length of the string...

```bash
$ strings -n 3 yarn 
ELF
tdd
/lib/ld-linux.so.2
GNU
GNU
U^TR
libc.so.6
_IO_stdin_used
putchar
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh 
QVh
Phh
UW1
l$0
D$8
D$4
[^_]
Sub
mit
_me
_fo
r_I
_am
_th
e_f
lag
;*2$"(
GCC: (Debian 4.9.2-10) 4.9.2
GCC: (Debian 4.8.4-1) 4.8.4
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
crtstuff.c
__JCR_LIST__
deregister_tm_clones
register_tm_clones
__do_global_dtors_aux
completed.6279
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
yarn.c
__FRAME_END__
__JCR_END__
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
__x86.get_pc_thunk.bx
data_start
_edata
_fini
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
putchar@@GLIBC_2.0
_end
_start
_fp_hw
__bss_start
main
_Jv_RegisterClasses
__TMC_END__
_ITM_registerTMCloneTable
_init
```

### Flag
Submit_me_for_I_am_the_flag
