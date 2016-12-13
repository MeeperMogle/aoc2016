import re

input = ('ORNXNQJQ(151x7)(5x9)OFIXU(27x3)(21x9)VDCYQELDJQUAFZUHFZVSU(34x15)(12x10)SEDIUUVFPEKY(3x9)NHR(1x11)I(15x6)(9x13)CMNDUYGYR(40x6)(4x7)RMNG(25x8)XPDSEYNCWFQFAKUMITWMBLMIK(7x11)(1x10)N(109x1)(101x15)(28x15)DYKYFCKDLFYAIHXSOAZKTPCPBUTX(18x13)SOZMWOSIQHVNMRZYYM(1x4)W(11x2)AJPKYMFRDJZ(11x11)SYIQBGHBNJL(26x9)(20x7)XLNTFHRYHLOYBBGMRPDH(269x4)(2x9)ZG(79x7)(24x3)UBTEBZLPYEDFINUQEQZUSXWY(3x5)IUH(15x10)LDDUEEJAWVGNRYA(3x5)FAO(6x3)ORDEIO(47x2)(1x10)J(2x13)DW(1x8)V(19x14)IJAAZPPGBZPFERJGOYI(103x9)(60x11)GKYOEUBZWAFDXEGWMPXZEOAQCUFCTJCXROPMNEFMJUWGBOUZRAXKRNHTBXHM(15x15)BTYXPHOQZXSBUVT(9x8)JQLNIDKMH(9x5)(4x4)BQRL(4207x15)(1464x12)(305x10)(159x14)(71x12)(24x14)(9x1)UJXIVHSUD(4x15)MAWK(26x15)(19x15)YFYDUJPUZQCKGVPOXKD(2x1)HN(2x6)GH(20x14)INJNODCLPWICQFIERROI(3x11)JUA(31x14)IUDVEHRATPGIEGELRDOZMBKZQFONCBD(130x14)(28x15)(22x7)(5x11)PHVKR(5x10)KVTDO(88x12)(8x12)POLKYDEX(27x8)(9x14)APMRPIHKQ(6x11)QTLLQU(1x4)R(29x3)(4x8)WBRL(2x15)JU(1x6)Y(1x2)U(1143x9)(364x14)(262x7)(6x9)EEJMXK(100x12)(5x1)RXXSO(5x2)VTESR(6x2)SXXSZL(49x1)OFIFQJKSCOXPXTHVWCUJVQMDBQELBLDYRKIGKHOEWRFNXNRLF(9x1)XRUFFMDVM(29x5)(3x8)VPW(6x3)WWFWRC(5x7)XMJEJ(46x9)ZBWGRECVBOPHVFQYBPOBHTPOMTYQGVZKQMKYEHCJYSNRQY(50x1)(10x5)SFPYPPQKDO(27x10)DNMTTNUGOQNAQLRBKDLNRVGRMLJ(23x12)(10x7)LCQWCIMTSV(1x12)X(15x9)JMJMKCIELUBETER(38x7)KWZVVWPBHKSBWMQWBJKCRHLIEHZSQBRAEOBRHE(130x13)(123x7)(75x10)(9x2)NUSXXITCS(11x2)JWHCFBJNEYD(10x1)QJNBNHNNDF(5x5)RWBYJ(11x10)GRRSDLTEZAW(35x9)EYHPPDLIWUITRPLKHXFBCUIQZZMYCDKWPNX(326x11)(130x1)(76x9)(9x10)TBCYBWJLT(4x8)HTQB(35x8)FUCOLJQAFSWAYTACMFRACVWDLZYRGSUMZAY(5x15)ZWHCN(17x14)CRUBDKGWUQCGGAIOS(10x7)(4x12)RWFL(3x9)TFR(27x13)(1x7)R(2x14)VY(8x2)DZMFRMGO(94x11)(61x15)(1x14)O(25x14)IKECWOPRWQBVRNEDQXWFMVBOI(15x10)QVTWMBNCISLOBJR(20x1)FIVILFBNIPNRXAWXGAMJ(32x8)LNPRYYKSLCXOEXFWZKAXERCQKDACFNYA(10x1)(4x14)WRAN(292x2)(168x7)(10x8)HQSTVLQCNK(89x4)(9x11)XCBGNGENA(22x5)BLUEARYFSAVBWTDGVHYWZP(21x12)KGRSTMCVPYJXIJWXVXREW(12x5)NKTUQMXCLFNL(17x10)UPUPBQDSHOXKHLGCR(10x12)ALIFHIZXQV(10x1)KEFBFHAOCG(100x2)(9x4)(4x9)MKGZ(80x5)(20x3)DQCKBWWUZDJICWUESBKY(14x9)EFXIDIWRKZTVUM(6x15)JRDKSE(2x14)AA(9x9)MJFTTZMTW(5x3)VLDNV(411x4)(397x1)(390x8)(46x4)(18x7)BLBFCJNGQWPSJGPOVU(16x7)(10x2)FFZWESCTXC(6x3)EUNIDH(56x14)(28x5)(2x8)CJ(2x1)EA(9x9)FLKGEMFED(10x9)OLOMVPKTRZ(1x5)R(202x5)(88x9)(6x3)VRZHGK(20x12)KKZGPZHKVMLDUKNRPDLL(7x2)CBDBTRO(3x15)XPR(23x3)EHEWCFLEUPCSTSISPKGXIMK(32x5)(16x12)KENYBOSVRILLLTVM(3x14)DYH(19x4)(7x8)FGHRXWB(1x15)E(39x8)(9x11)XRLWASPXI(17x10)RNFIHAQMBBELSLNCT(49x1)(36x4)(18x2)QKRMYMDFPSVDXUXXCH(7x3)SBFHWUF(2x6)BD(2x6)HN(1047x3)(450x2)(10x4)YQQDOELWCI(48x15)(25x7)(8x5)KUKZDUYU(7x6)(2x1)KQ(1x4)K(6x3)INDERJ(284x5)(92x7)(86x4)(13x1)PSVECPHBPYEPJ(3x15)JEY(35x8)RCTZOHPJAICRPRVAYZZLUKRZPOOPFCBCPAQ(4x9)TETC(2x11)ZV(179x5)(95x6)(8x9)HUGVMXOT(9x10)MFDYGPUWF(12x2)PSBNZPCWSANA(6x1)GICWEI(32x9)JCBCGJIMZTQUSVQDRHWMSYJYUHJIVYIV(71x13)(15x3)SXTGVVIWXDWZTZO(9x2)RASQPEQUN(7x10)TPHSDTV(7x15)EPAHSDZ(5x6)BIOZT(7x4)KYMJLYA(69x11)(63x5)(3x9)XSS(37x9)HTZKRPESNZRIWPGWAPHBOIOWAWFHWMIXWYQQC(7x6)(2x1)FA(273x3)(245x12)(39x9)(8x13)WCKBPVRZ(18x10)(11x10)VHBAIPPIWXD(2x3)XD(1x11)Q(6x15)WCPPQC(167x1)(23x15)DYHQGULKPISILTRIXNEJZAV(65x12)(2x9)FZ(14x9)WWCTYVLVAOZDAG(15x11)CZYGTNAELLIRKYW(10x6)IEXFBJJCLQ(42x4)(9x14)XRPJHVVME(6x8)XAVNCD(10x9)IBVGVWIFUD(11x7)(6x6)LSMIRR(14x4)LFACCTXVWLEDWE(287x5)(280x2)(273x1)(7x14)(1x15)U(109x12)(7x1)TPNMYVS(46x8)TWTINTRPDOQKPDPZNKXIVISRQTZODBXMSPPZKCQFAYCJCS(5x11)AKNKA(18x14)DKSKSQUAUTPZPNHIWP(4x7)DOMY(56x3)(6x6)JBJORX(7x11)IDJWUCZ(26x1)XMRHHVJEZBAIOCBKTLKEWRQHWR(46x3)(6x8)JDOJMU(5x6)ELYWH(1x1)M(1x13)Y(7x9)XRTOLWT(22x11)PXZRLOPHTRSXFEGYCCCKOZ(1x6)I(4x11)OPMW(2x11)ET(1244x13)(8x9)(3x8)ABP(1x13)B(188x1)(6x9)(1x5)H(161x8)(115x15)(15x6)(4x8)YQCB(1x1)L(73x9)(2x15)GX(25x4)NTANLQJGDHTCOIRAFZAKXQHVB(1x3)R(10x5)VDXVAGTAGQ(7x3)NKCTQVK(3x9)RRQ(1x15)C(31x15)(1x2)G(19x2)OAUAOISPSPTMKOGJEAV(4x1)DQTV(229x5)(2x4)EP(124x5)(117x6)(109x14)(16x14)UDUBGHIWRGGHYVJU(2x1)DG(7x14)XZCOKGR(4x15)XDVD(49x10)HIHUJRXURZHGHWJMFTGUQUBGCJVLZSGLDIANTUIKYZWXHMAZY(84x14)(6x15)IEUICQ(13x5)HXIRLHFWXDSIB(2x13)XU(39x4)(25x10)(11x14)MWHAQQMPPVR(1x13)R(2x9)UL(786x5)(38x10)(1x12)S(25x9)RRXFLAJRHOUZPDTBWKIZHUNGA(471x12)(54x8)(34x14)VJZSILTGZWMCZLOJSZHTQVVAZSPWHAKVFO(8x3)XCYTBHDX(221x9)(60x1)(1x2)M(17x13)PIRWGCEZQNSPPUBHK(23x10)YJEVBSPQYKPLPDOSCEHYSSA(78x12)(2x6)YY(21x5)TMWGVWVOZDOFGCFEZJRJR(32x5)ENWXNGFHIYQHCBWQEDTMBOWQKJIHAZHY(1x1)E(18x9)(2x1)OD(5x11)GGATR(32x11)(13x9)VZVAFSADAUIGI(8x2)JOUUXRCU(1x11)I(8x7)(3x8)PCV(75x3)(46x4)(28x9)PJXDTVYIRKASKJMXDIGAXSQPMPWK(6x11)SUYPHC(4x13)CBMV(8x7)QAUWLDLP(83x8)(19x7)DDNWFTSHJSTPWECIXWZ(6x5)EQWGSJ(1x5)O(20x6)(13x10)MNFVFUCESZDMF(9x15)(4x3)JZSU(7x12)(2x9)UZ(228x2)(220x15)(49x2)(1x10)C(5x9)TCPJZ(6x7)FJSPSS(4x14)FYQF(5x15)XBWKH(75x10)(5x15)KTHBO(12x5)LLZEFONZKCBI(28x5)RGMNFEEHBHZJKTMPVEPHIOJUXOMB(7x9)YWTZNCT(60x14)(3x10)DAN(15x6)BHOSLMFSEQKOGEX(1x4)D(17x11)SULIDVKKLXIWAJXRK(2x7)PX(4x1)TKPO(9x8)QFXUEZUGP(2331x2)(2323x8)(202x13)(10x13)(4x14)GFSR(178x4)(101x11)(21x9)(5x9)SWRRL(6x8)TYXYPJ(68x5)(4x10)QMJZ(19x15)APBTUGYPJQFQODZRNAC(5x13)YIVAO(14x14)QHWPZNQSRZJIEC(63x2)(32x10)(5x4)EVMQL(15x12)SAOYGPDXFSDOBTB(6x8)(1x5)C(7x13)MILUDKF(144x5)(3x8)PLQ(129x7)(27x3)(7x13)QLVZTAJ(9x4)JNLNRKPXA(4x13)EEXX(17x9)(11x9)SYQBWQASJPK(57x8)(29x8)(15x11)CFVXGJKXAAKNRRT(1x15)A(1x4)C(10x5)EFFLNXDEVJ(664x6)(357x6)(82x8)(7x12)LPCKKIX(55x10)(6x4)KXJNIR(2x4)IH(5x6)VIUMV(11x10)TCNXEQRMQJZ(4x7)DREZ(2x8)IV(119x7)(21x13)RHDEMDBNRPLOTSZRKZSHA(47x2)(22x2)ZADHZNUARPTFHKEXJKCWXY(7x6)OACRTYP(1x15)P(31x10)(5x4)VSWJT(7x1)IGAMFHI(4x3)GOCU(26x5)(19x13)(12x15)WGYBKVRPMWJT(15x7)IFUICWKGGCLHCOO(83x12)(62x8)(20x10)TJBGZCIWVKOROYITLBUA(7x11)UDSMGLK(6x3)FWPTWW(6x4)JECWEE(9x13)CUQMJOFWT(292x11)(68x14)(61x13)(28x10)ZRYXMSXXTLGDYHOVDRDVOCFJTCXJ(20x7)HZCFVXJATHXTNPHWFSIS(65x4)(11x6)BETMULBEIND(3x11)VLU(25x5)UYRFOHJXRRSJXEFEOPROCVNOA(3x4)GQJ(95x8)(81x11)(30x12)FXPGOAGXMVWAMAKJTQKJEUZNGCKDXU(10x5)YFDYGXCFTD(10x5)USWAFQFFSA(6x10)ZFVKMB(2x8)SF(16x8)MZPGUBATXFXXJOJS(17x4)AJTTIOULZONRGGMLK(448x2)(28x11)(22x2)(8x13)(3x1)TMQ(2x13)IP(5x6)AJJXN(290x1)(109x10)(5x12)CUMMS(7x7)UEWYDSN(59x12)(2x12)FP(26x3)LWFPYEPAANDDLIOJQBYCRRQYRT(1x2)O(7x10)RXDHAJH(14x6)(9x6)PQLSJTFAO(124x4)(56x12)(12x10)DOOJHOYDOTLM(10x7)VKUFQDGCPT(6x9)ONBPUY(5x5)CMPUW(5x13)WWWWM(16x9)TOPYYTZBFGFAXYBO(14x15)(8x10)FPVBQPNJ(1x15)O(18x1)UTQYAKMVOBJZDLTOVO(12x3)YHILDGGCGZXZ(20x7)(13x15)RVSYRCEYESCUC(73x10)(21x5)(15x4)EHQBVPUAJWTOZKA(22x12)FIWIHPWFDOJTMAXRCKCJZE(11x5)(5x15)PDHSQ(828x13)(1x8)P(161x8)(154x4)(11x3)DAFIIEMOBYZ(6x1)EGJWXU(107x7)(13x2)SRTDQRBOGITPI(6x2)VWSTKU(23x5)GJXMEBCGSIYQNMFLISIUFTB(1x2)D(36x8)GKPPJHVMOOTOCTUHRGVVQUKNHRCZNINYLJGB(6x11)EFSGDL(327x12)(6x2)QAAXCM(5x9)YVLGN(86x1)(10x1)SVFCLDTQEO(2x4)OA(17x15)OAEGSJHUTEFJXDOTD(7x7)HGXVBHJ(20x15)(2x6)XQ(8x5)KDXCQOFM(90x11)(14x15)(9x9)DTJSQPKYW(25x7)(12x11)SYLBSZEMQSQA(1x3)S(11x2)(5x13)KWHSE(4x7)MFSC(7x6)(1x12)F(110x2)(10x1)UIIOJNJJJI(88x8)(10x10)PQCUFWXHMC(15x12)OVVASAWDIIOZYIT(17x3)NLLLZIVNOIVEHGXDP(19x11)CDJEUHEPCUEYVLGYLTJ(311x11)(165x1)(16x7)MUMPDQFLGFEGIYLU(9x11)(3x11)FNP(1x14)U(60x4)(4x7)KDWX(4x1)LKMS(27x11)MIELWFKZJUSUYBARAGTJAZIBEDH(3x1)LDI(48x15)(10x15)DUUYAIZHKY(5x8)KEMNC(14x10)HZTAHRSCICOTIR(4x13)AUNU(45x2)FRDBNRZYFZLCAIEVZWSAIMLGBCDSBHXFPWRPYJRQHNWUZ(28x8)TCHELUEWWRHMIGBKEUCWBTIEVNCB(37x10)(30x11)(6x9)PLWKRH(2x3)PL(7x2)MAFSJHV(6697x8)(172x15)(164x10)(1x9)N(151x2)(7x2)MOYJQSA(24x4)BSZRAIBTDPFAAHQWOWDJJRCW(34x10)(2x15)QB(1x1)T(4x3)ALVX(6x7)SQFSKZ(2x11)JX(54x2)(47x14)(6x12)HOALAK(28x10)DGCVKLTWNKGAGRGSWPVEUGRDAGWA(2577x12)(88x14)(82x9)(48x2)(41x11)(4x5)KAVK(15x4)LCMPETDQZUWBRCL(6x9)CFZJGS(7x15)PGVNKAY(9x12)(4x4)NHID(827x3)(259x9)(153x12)(27x11)(21x4)PQNSUYEFBRAAVCJFJPPGZ(13x4)(7x10)NNSUBSG(70x11)LOGUFNQNLSWWQXBPQIWNJIEDRFUCRCUAVANHFGDEMQZRGSITBSBLZXVWJGXPPDZEXZQCEU(7x10)DTIEEXA(4x13)DDNZ(44x13)(37x14)(8x14)NIJOMVGP(17x1)MDXVVVWIZSXMSGJMC(4x4)ARFY(31x11)(10x14)RVZUREXEUI(1x7)M(3x5)LXC(170x5)(114x3)(83x3)(19x10)UUCHMGESOOTJCTEJVRM(3x5)ZCP(2x10)IU(25x6)TNLNLUTXNPNDWMXGVVGIPVWJL(4x12)JAAA(13x1)UFQFFPMZGZNNN(1x1)V(27x5)EDPBYCEAMMWAIPWUZODVDAWPWIJ(10x1)(4x10)VJHN(73x13)(66x12)(5x1)TAFQR(11x5)(6x8)ATBQTY(5x8)KZYJI(23x1)(17x3)VSDOKMWKSGRRIRXWF(297x5)(11x6)HTGQDOGJQSJ(49x13)(43x1)(8x5)ULVVUCJI(6x11)JAITVW(12x3)ISRQLAPACLXU(25x2)(19x7)(13x2)SRBHDIAPWUMER(51x9)(45x1)(8x9)ADOZRIJD(13x15)JXWDDHBYCJKMO(6x10)SKLMKL(129x8)(111x2)(5x10)ATJGD(22x6)OLATWNGTXFJMTWCJQAQDDA(19x1)WLYAFVAKQECTNXJRBVH(20x11)DDWDXGQEZBKJBDJBAKJB(14x5)TIZKGCXPPUBGSJ(5x14)SEHYY(1410x15)(148x5)(24x2)FHQUELWXQDUWLIBTXEPSQTJQ(111x3)(40x13)(6x7)ZAWWAD(2x15)GI(3x6)XJY(7x14)SCZWIKT(10x1)WMCTELCITD(15x12)(2x8)OD(3x3)IKM(12x2)(7x4)BEEDJSC(2x15)SZ(303x5)(89x2)(70x4)(3x7)ATQ(9x4)WSWYIUPAG(12x8)KDWAUNHURPWB(3x15)ESP(15x7)DANNZUDKDFXXSBO(7x12)VUNUHBI(1x8)M(180x9)(66x1)(20x12)MOUJOXCMCZUPVKVXPKUB(27x5)QHNMIHMVJVBBVCDGHPYOWRHTCLT(1x8)Q(22x13)ADGXYCQHWNAGCLWNPXBPIX(73x9)(1x11)J(27x14)ANTTYLYVSVWEAPXPGRRVWVINHFM(7x10)ZDBZWVE(3x12)ISL(5x4)YDXBZ(9x14)XBPBWAQTR(407x3)(186x1)(36x10)(1x2)W(23x13)DBNCARJKKIAWVQVKNOIPSJO(57x2)(6x9)VKZMPB(3x2)JIZ(22x2)AQWQZQOKXLPZSJTNBJKCXL(4x12)OAOJ(8x8)(2x10)PT(29x3)BKPFZBRCXVJUJJHVOIMJELFFHHBUR(26x5)WUACSRCIRADIQKCXKEESRJNWKU(10x9)RBSMRSUWMK(177x3)(1x10)Q(28x8)(5x5)PQQGD(6x13)LAGOEK(1x5)C(71x13)(16x12)IIAWONMLGHMCHWIH(19x11)KEYESARBBXHWWQWPQVC(1x11)A(9x12)LMADFIHXJ(6x5)MZVRQU(40x12)TOSAJVXJHKVWJKLTVBIUKKESOFCKFOPSXHYCMDXQ(8x15)XGHEISVJ(68x5)(62x3)(4x7)OOWZ(7x15)QNNVWUX(5x10)GSLOA(14x8)(1x8)B(3x3)HJL(3x11)EIK(450x6)(101x9)(30x8)(2x5)MM(17x8)GHTHOCTDDQAYBUVWP(59x8)(1x5)R(3x11)HYR(21x2)STLZXNENUFTGYWNQJHFUK(10x10)NGMEAWPFBI(28x3)LNDWFXKPRAOWKJHWZZIYLJLOOBKK(110x6)(14x2)SALGMMEIINEJOU(40x7)(4x13)AIMA(5x12)GSAFV(13x7)CSLJJRZIBBUMF(21x1)(15x9)THPSZDCPWASRUYR(2x5)EE(5x7)XDUPK(13x10)(7x13)SFWIYYQ(163x10)(26x15)(13x9)HQJQXZQCIHSAE(1x15)K(4x15)FMWB(9x12)SQVQTEWMD(41x3)(13x1)EEYHHJQCDSYRO(9x2)YCDDFHWTG(3x9)LGW(51x12)(7x14)OITBFQF(8x13)FZVMIWUM(9x8)XTZCNFOTE(4x15)KTHY(221x10)(213x14)(32x3)(26x3)GEUNPCYFYLTFFXOKWXFBDYLBMK(77x1)(41x14)(7x11)XBMCCZD(21x11)KFOJGBJCEHPTKBLUSTERX(10x4)IZWNLBDABA(8x3)IVDWYIMO(50x9)(6x5)(1x1)H(4x8)VDKE(2x5)QE(17x3)(11x7)KGYMJEMQVWS(9x4)EVWJYLBBQ(16x8)XZDDQZQPCOLVIYGD(3001x2)(724x14)(235x12)(227x11)(25x5)(1x10)N(3x4)QSO(5x3)XPKCV(24x8)(11x10)XXOIOGOKIOD(1x8)B(88x4)(1x12)I(10x6)CEIKKPKUJG(1x11)Y(6x8)QAYNKJ(41x7)BGKQCYZZGRQGCNXSGYHAXMWIJOPDKLMAQRKGFRBML(66x9)(14x12)YTKTEIISOWYZWB(3x13)UDK(12x2)PXDYSSCHAFSE(2x2)DA(6x1)UZSORT(309x1)(107x1)(81x11)(23x4)UHLCPASWMUWBQPYJSUHUFEO(5x1)NTMAV(26x7)JDNTOBRNEUELJIISZGKNRYSBRE(4x10)FVKZ(13x8)SBNXXTKLMDHII(138x4)(62x12)(55x12)OMRRSQWFPEAXAXHFHHQBWGCESBLWZBVYEQQKYRGILBNJJCAOXFHDIXU(19x13)(4x5)CVBF(5x9)EBLEV(15x1)(9x13)BATHCHMGP(16x1)BGSXRPQUKQJYDIPV(44x3)(8x1)(3x1)EWQ(7x12)JJIVUYJ(12x7)XJSYYYTSZBHD(7x14)EDHTGLH(144x13)(130x4)(12x7)(6x14)CYDLYL(43x2)(4x10)DOTG(4x8)ELJI(6x6)QGMRSQ(1x4)K(2x9)GS(40x2)(11x10)CDHAMRCSTVC(8x11)WMZDTRTD(2x14)XS(11x4)IXUNDJVBLSO(2x3)CH(7x7)(2x5)NF(1015x9)(204x1)(20x10)GPKSBZZRRZGMFICXNMIX(141x9)(24x9)NXNCFLIWVVVQNVKDRUTQYNJB(3x8)AXD(33x6)MDGPOLEPZEUNBDWGBSAFRPEMTKUXIJDRA(33x11)(2x15)PY(5x1)XYUAI(9x14)UPOUZTFRQ(17x10)YAMBZLTZMBSRFZOUK(5x10)NXKJE(11x15)GNJTBTSXLTN(299x9)(29x1)(22x10)(5x13)FSAYZ(5x14)MWJOX(178x9)(79x14)(21x12)WXTCOEECSKHDITBOAAVSF(6x15)INXWKB(8x11)NTSEQSMQ(19x1)UTQUQGUDXSFROLQWKVZ(76x6)(3x2)QOL(10x15)UIGYPYAWRR(7x7)JEELSVH(13x12)RUBSHAXAWQGYF(12x12)PGQUXPKEKXRN(4x15)BQEB(8x4)(3x1)AVE(59x15)(11x11)QGBFDCZTADF(22x8)(7x7)RJEZNHA(4x11)MMJN(8x7)(3x7)GNT(174x1)(166x12)(17x2)ZDOBQSATWXMNNJDCV(17x13)(10x14)CATNORVTYK(95x10)(9x5)LROSBZBVM(29x2)ZQBDHDVQJGZTGKDBOSHXOCVXYOSKC(22x11)FXLGIAQRSIJQCGUQPFJXFM(3x8)HSE(3x11)JVV(11x2)(6x7)YCATPH(206x5)(133x6)(31x8)(8x5)YTYSRRBZ(4x13)UYBY(3x6)SJW(32x4)ZCNRDWQGEMLBOCMJMCAJJVJPLIQXSTSG(52x3)(12x10)ENCLYDJSGEYW(13x15)EXRYDALLRZKCF(8x1)RIVKPAAB(8x14)GUSBQGHU(46x2)(1x5)P(34x8)(16x3)GDVLVDXNKOCDWQJI(6x15)YGGNZJ(98x6)(91x10)(11x5)RVKZVECGFPV(8x12)(3x7)URB(54x1)(11x12)JPMMFXPJPMQ(5x1)ZKRGP(19x13)ZJIYXFENCFNAFOEFUNL(1225x12)(534x15)(214x13)(64x15)(5x7)PZQBH(25x10)XSZONMJVANCJZOJPAAEJSRYGT(16x5)PQPCLAYGZUDSQKTZ(83x8)(40x6)ZKUMBQGMGPGEAKSJHFSIPNWEKXZEHBJUUSCVWYMY(10x5)CMXYJOWZZN(6x1)WPARZQ(4x14)FAYY(16x1)(1x11)E(3x12)MLF(25x11)(3x8)BRT(10x14)OGKXRSWWPD(4x1)VFBM(227x12)(150x2)(25x10)YFBSVADMLPNYAIXAPMBRZPTCO(8x14)PKGEMLYV(50x10)DKUPPNRQKKWAJIQCFKGQVRSXTUWPVNQZESPGLNQWMVMAOCORMP(9x6)HVKQYKZAH(26x10)RQQPTHCFQFHIBMEATIAVVKWDWG(57x9)(8x10)QVILTCPK(36x13)LUDTUSNBRJNJCTXOFFMWIMAMWBKXHMMENNSW(2x7)ZQ(62x5)(25x8)(5x15)GCZUZ(9x1)JPDRQMLTB(24x13)YTTGOHFCVHRRGLESEARVNFPQ(178x5)(42x2)(21x15)(8x5)RPZICSEL(3x4)YIL(8x13)(2x11)GF(84x11)(70x2)(7x5)MWWDPMK(7x11)TEYJOFJ(31x1)TWNBXEDRILLPRUGJDBIVBFYNVHGLUED(3x8)VDU(3x9)YYV(7x4)(1x12)L(21x1)(1x4)M(1x8)J(4x3)XJGN(491x9)(148x8)(36x3)(2x9)MG(13x11)EDWPZURXZWLML(4x1)VRBX(31x11)(14x8)KBLQBMRGRGKHCT(5x14)PRDLH(3x8)CQB(32x15)(10x15)RLWBNSAEHH(3x3)HPB(2x2)PA(15x2)TKPIZXDBJJMAZDR(133x8)(1x6)B(83x8)(13x10)WNSKNXUSTCDKE(4x8)NMAW(6x6)EJRNHD(4x14)MLJN(27x5)ZQBFSJWECOPVETZPGXQJPPDQZEL(22x1)(16x1)ZSEPLZISVDFRGRJB(4x13)YRXG(39x2)(33x7)(16x9)HMRXYWRBVITBVWTG(6x2)LCYRSW(123x13)(31x12)WVTWWQZUYGBJOSPKLUQTAGWXXURUDLI(34x10)(7x5)ZTTMEQS(2x8)YX(9x13)ROIYTCKSX(28x13)(3x9)WPV(13x14)PQHWCFNXKFFOH(3x15)EUZ(14x7)(8x15)UHHVOLEJ(914x15)(782x12)(448x5)(118x6)(26x12)(4x12)BLTT(10x2)REYZXYJJFQ(39x8)(8x6)XEWKRGZT(3x8)ECB(5x9)GOBWQ(3x2)KKM(34x7)(18x11)QSQRCJXLCKUYJBPSWG(4x9)XOSJ(34x5)CIABSNSBNQQKAARJOOETKSXJIPOFQOMAPK(24x13)(3x7)ADL(10x3)RVSLAIXAJJ(67x7)(52x9)(3x2)AJH(3x6)OGK(4x9)SQFL(1x1)T(14x14)BQZZXEWSTOKEUA(3x13)HBM(171x14)(25x9)YKLMFOEYQHSODISORNEKDIGVY(12x6)(6x13)OFJBKW(53x7)(21x11)GINJQDIXMAWRHIHJLXFIP(19x8)SVTFKYTLPWYEWWFIUPB(16x12)(2x1)PB(4x8)TMWZ(33x15)(5x3)QBMUH(10x5)UHNESLDFMY(2x4)WW(9x2)(4x7)QTKW(94x10)(47x10)UUVWDQXOXQUFEROVLOZRXIHEPHTWRPSGHLNSYGNIVHEDQGV(34x3)(21x4)(7x9)IMCZEIB(4x2)TNMA(2x9)DM(192x6)(2x7)ZF(2x3)VU(6x13)DODXJG(158x15)(1x4)K(42x12)(2x8)RM(4x6)YMIM(5x2)BXKIG(10x1)ZWQMIAOBEY(78x8)(7x1)XHAETJV(28x1)QPKULGVENLMJWWEHOROJEESLKYTA(3x5)XMZ(18x1)FZBLVDOKGEZKOBICEO(13x9)MWICPPUEWVWKH(7x10)KVNGSWM(116x10)(26x3)(20x8)(8x12)SSVBYWJX(1x9)H(77x14)(12x3)OWHWKICESREK(1x11)D(46x3)(11x5)(5x15)ORJRA(1x13)K(16x3)XRJXBYVIUITRPPYRRNHU',) # trailing comma (,) required to treat single element as part of tuple

input2 = ('ADVENT','A(1x5)BC','(3x3)XYZ','A(2x2)BCD(2x2)EFG','(6x1)(1x3)A','X(8x2)(3x3)ABCY')

input3 = ('(3x3)XYZ','X(8x2)(3x3)ABCY','(27x12)(20x12)(13x14)(7x10)(1x12)A','(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')

inputToUse = input

def decompress(text):
    print(text)

    # Start with empty decompressed string
    decompressed = ''

    # Loop through original text
    index = 0
    stopIndex = len(text)
    while index < stopIndex:
        # Find the next parentheses in the text, from current position
        try:
            startOfParentheses = int(text.index('(', index))
        except:
            startOfParentheses = -1
        print('startOfParentheses:', startOfParentheses)

        # If THIS is the position of the next parentheses...
        if startOfParentheses == index:
            # Find the end-position for the parentheses this is where the content to be decompressed starts
            endOfParentheses = int(text.index(')', startOfParentheses))

            # Find the contents of the current parentheses
            parenthesesContents = text[startOfParentheses : endOfParentheses + 1]

            print('endOfParentheses:', endOfParentheses)
            print('parenthesesContents:', parenthesesContents)

            # Extract how many characters that should be repeated, and how many times
            characterCount = int(parenthesesContents[1 : parenthesesContents.index('x')])
            repetitions = int(parenthesesContents[parenthesesContents.index('x') + 1 : len(parenthesesContents) - 1])

            print('characterCount:', characterCount)
            print('repetitions:', repetitions)

            # Copy the Amount number of characters, starting right after the parentheses
            repetitionText = decompress(text[endOfParentheses + 1 : endOfParentheses + 1 + characterCount])
            print('repetitionText:', repetitionText)

            # Append the characters onto the decrypted text Repetitions times
            repeated = 0
            while repeated < repetitions:
                decompressed += repetitionText
                repeated += 1

            # Set next index to right after the repeated character(s)
            index = endOfParentheses + 1 + characterCount
            print('index:', index)

        # If this is not currently the start of a parentheses
        else:
            # find the next index to go to either the next parentheses or (if not present) the end of the string
            # Read the text between current position and the next starting position
            nextIndex = len(text) if startOfParentheses == -1 else startOfParentheses
            textUntilNext = text[index : nextIndex]

            print('nextIndex:', nextIndex)
            print('textUntilNext:', textUntilNext)

            # Add the in-between-text straight onto the decompressed text
            decompressed += textUntilNext

            # Jump to the next position
            index = nextIndex

    return decompressed

for compressedWord in inputToUse:
    decompressed = decompress(compressedWord)
    decompressedLength = len(decompressed)
    print('word = decompressed (decompressed len): ' + compressedWord + ' = ' + decompressed + ' (' + str(decompressedLength) + ')\n')
