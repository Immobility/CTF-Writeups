One of the most simplest ones for the Reversing challenge. Once you download the binary "reversing1" file, head over to the terminal and type ``` strings reversing1 ``` to pull up: 
```
/lib64/ld-linux-x86-64.so.2
CyIk               @��	@*� � �t
libstdc++.so.6                  @���    @- I��
__gmon_start__                                @� ��x `��� `� `1�� `>
_Jv_RegisterClasses                                                 @eN `ZvV!`���� `�p	@#�
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTablederegister_tm_clones__do_global_dtors_auxcompleted.7594__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryreversing1.cpp_ZStL8__ioinit_Z41__static_initializat_ZNSaIcED1Evruction_0ii_GLOBAL__sub_I_main__FRAME_END____JCR_END____GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___init_array_end__init_array_start_DYNAMIC__libc_csu_fini__gmon_start___Jv_RegisterClasses_ZNSt8ios_base4I_ZNSt8ios_base4InitD1Evibc_start_main@@GLIBC_2.2.5__cxa_atexit@@GLIBC_2.2.5_ZNSt8ios_base4InitD1Ev@@GLIBCXX_3.4_ITM_deregisterTMCloneTable_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@@GLIBCXX_3.4_IO_s__gxx_personality_v0erTMCloneTable__data_start_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@@GLIBCXX_3.4.21__TMC_END___ZSt4cout@@GLIBCXX_3.4__dso_handle__libc_csu_init__bss_start__stack_chk_fail@@GLI_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_char_traitsIcESaIcEEC1EPKcRKS3_@@GLIBCXX_3.4.21_edata_ZNSaIcEC1Ev@@GLIBCXX_3.4__gxx_personality_v0@@CXXABI_1.3_Unwind_Resume@@GCC_3.0.symtab.strtab_ZNSaIcEC1Evterp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.gcc_except_table.init_array.fini_array.jcr.d_ZNSt8ios_base4InitC1Ev.comment
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev
_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
_ZSt4cout
libgcc_s.so.1
_Unwind_Resume
libc.so.6
__stack_chk_fail
__cxa_atexit
__libc_start_main
GCC_3.0
GLIBC_2.4
GLIBC_2.2.5
CXXABI_1.3
GLIBCXX_3.4.21
GLIBCXX_3.4
AWAVA
AUATL
[]A\A]A^A_
QUFBQUFBQUFBQUFBQUFBQQ==
Hello! I bet you are looking for the flag..
I really like basic encoding.. can you tell what kind I used??
RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn
Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=
Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==
WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn
;*3$"
zPLR
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
completed.7594
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
reversing1.cpp
_ZStL8__ioinit
_Z41__static_initialization_and_destruction_0ii
_GLOBAL__sub_I_main
__FRAME_END__
__JCR_END__
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__init_array_end
__init_array_start
_DYNAMIC
__libc_csu_fini
__gmon_start__
_Jv_RegisterClasses
_ZNSt8ios_base4InitC1Ev@@GLIBCXX_3.4
__libc_start_main@@GLIBC_2.2.5
__cxa_atexit@@GLIBC_2.2.5
_ZNSt8ios_base4InitD1Ev@@GLIBCXX_3.4
_ITM_deregisterTMCloneTable
_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@@GLIBCXX_3.4
_IO_stdin_used
_ITM_registerTMCloneTable
__data_start
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@@GLIBCXX_3.4.21
__TMC_END__
_ZSt4cout@@GLIBCXX_3.4
__dso_handle
__libc_csu_init
__bss_start
__stack_chk_fail@@GLIBC_2.4
_ZNSaIcED1Ev@@GLIBCXX_3.4
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@@GLIBCXX_3.4.21
_edata
_ZNSaIcEC1Ev@@GLIBCXX_3.4
__gxx_personality_v0@@CXXABI_1.3
_Unwind_Resume@@GCC_3.0
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
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.gcc_except_table
.init_array
.fini_array
.jcr
.dynamic
.got.plt
.data
.bss
.comment
```

Now the specific part of the string that looks suspicious to us is:

![](https://github.com/Immobility/CTF/blob/master/tamuctf-2019/images/reversing.png)

This specifically tells us that it used something encrypt the message, by looking at this, it looks pretty close to base64 so after we decode in an online decoder, we see:

![](https://github.com/Immobility/CTF/blob/master/tamuctf-2019/images/reversing2.png)

Seems like a bit of the decryption got a mixed up, so lets remove the parts that have been decrypted, then only ```Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==``` should be left, by decrypting we get ```gigem{3a5y_R3v3r51N6!}```!
