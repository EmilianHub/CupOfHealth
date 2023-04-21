PGDMP                          {           CupOfHealth    15.2    15.2 B    S           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            T           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            U           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            V           1262    16398    CupOfHealth    DATABASE     �   CREATE DATABASE "CupOfHealth" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Polish_Poland.1250';
    DROP DATABASE "CupOfHealth";
                postgres    false                        2615    17095    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            W           0    0    SCHEMA public    COMMENT         COMMENT ON SCHEMA public IS '';
                   postgres    false    5            X           0    0    SCHEMA public    ACL     +   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
                   postgres    false    5            T           1247    17097 	   tag_group    TYPE     �   CREATE TYPE public.tag_group AS ENUM (
    'disease',
    'welcome',
    'question',
    'goodbye',
    'thanks',
    'noanswer',
    'name',
    'mood',
    'specify',
    'few_questions',
    'end_diagnosis',
    'leczenie',
    'opis'
);
    DROP TYPE public.tag_group;
       public          postgres    false    5            �            1259    17121    chatbot_patterns    TABLE     �   CREATE TABLE public.chatbot_patterns (
    id integer NOT NULL,
    pattern character varying,
    pattern_group public.tag_group
);
 $   DROP TABLE public.chatbot_patterns;
       public         heap    postgres    false    852    5            �            1259    17126    chatbot_patterns_id_seq    SEQUENCE     �   CREATE SEQUENCE public.chatbot_patterns_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.chatbot_patterns_id_seq;
       public          postgres    false    5    214            Y           0    0    chatbot_patterns_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.chatbot_patterns_id_seq OWNED BY public.chatbot_patterns.id;
          public          postgres    false    215            �            1259    17127    chatbot_responses    TABLE     �   CREATE TABLE public.chatbot_responses (
    id bigint NOT NULL,
    response character varying,
    response_group public.tag_group
);
 %   DROP TABLE public.chatbot_responses;
       public         heap    postgres    false    852    5            �            1259    17132    chatbot_responses_id_seq    SEQUENCE     �   ALTER TABLE public.chatbot_responses ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.chatbot_responses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    216    5            �            1259    17133    choroby    TABLE     h   CREATE TABLE public.choroby (
    id_choroba bigint NOT NULL,
    choroba character varying NOT NULL
);
    DROP TABLE public.choroby;
       public         heap    postgres    false    5            �            1259    17138    localization    TABLE       CREATE TABLE public.localization (
    id_loc integer NOT NULL,
    woj character varying,
    miasto character varying,
    choroba_id integer NOT NULL,
    session_token timestamp without time zone NOT NULL,
    created timestamp without time zone NOT NULL
);
     DROP TABLE public.localization;
       public         heap    postgres    false    5            �            1259    17143    localization_id_loc_seq    SEQUENCE     �   CREATE SEQUENCE public.localization_id_loc_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.localization_id_loc_seq;
       public          postgres    false    5    219            Z           0    0    localization_id_loc_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.localization_id_loc_seq OWNED BY public.localization.id_loc;
          public          postgres    false    220            �            1259    17144    objawy    TABLE     e   CREATE TABLE public.objawy (
    id_objawy bigint NOT NULL,
    objawy character varying NOT NULL
);
    DROP TABLE public.objawy;
       public         heap    postgres    false    5            �            1259    17149    objawy_to_choroba    TABLE     i   CREATE TABLE public.objawy_to_choroba (
    id_objawu bigint NOT NULL,
    id_choroby bigint NOT NULL
);
 %   DROP TABLE public.objawy_to_choroba;
       public         heap    postgres    false    5            �            1259    17152    patterns_responses    TABLE     \   CREATE TABLE public.patterns_responses (
    pattern_id integer,
    response_id integer
);
 &   DROP TABLE public.patterns_responses;
       public         heap    postgres    false    5            �            1259    17155    profToChoroba    TABLE     o   CREATE TABLE public."profToChoroba" (
    id_choroba bigint NOT NULL,
    "Id_profilaktyka" bigint NOT NULL
);
 #   DROP TABLE public."profToChoroba";
       public         heap    postgres    false    5            �            1259    17158    profilaktyka    TABLE     b   CREATE TABLE public.profilaktyka (
    id_prof bigint NOT NULL,
    profilaktyka text NOT NULL
);
     DROP TABLE public.profilaktyka;
       public         heap    postgres    false    5            �            1259    17163    user    TABLE     u   CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying,
    password character varying
);
    DROP TABLE public."user";
       public         heap    postgres    false    5            �            1259    17168    user_disease_history    TABLE       CREATE TABLE public.user_disease_history (
    id integer NOT NULL,
    user_id integer NOT NULL,
    user_symptoms bytea NOT NULL,
    disease_id integer NOT NULL,
    created timestamp without time zone NOT NULL,
    confidence double precision NOT NULL
);
 (   DROP TABLE public.user_disease_history;
       public         heap    postgres    false    5            �            1259    17173    user_disease_history_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_disease_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.user_disease_history_id_seq;
       public          postgres    false    227    5            [           0    0    user_disease_history_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.user_disease_history_id_seq OWNED BY public.user_disease_history.id;
          public          postgres    false    228            �            1259    17174    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    5    226            \           0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    229            �           2604    17175    chatbot_patterns id    DEFAULT     z   ALTER TABLE ONLY public.chatbot_patterns ALTER COLUMN id SET DEFAULT nextval('public.chatbot_patterns_id_seq'::regclass);
 B   ALTER TABLE public.chatbot_patterns ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214            �           2604    17176    localization id_loc    DEFAULT     z   ALTER TABLE ONLY public.localization ALTER COLUMN id_loc SET DEFAULT nextval('public.localization_id_loc_seq'::regclass);
 B   ALTER TABLE public.localization ALTER COLUMN id_loc DROP DEFAULT;
       public          postgres    false    220    219            �           2604    17177    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    226            �           2604    17178    user_disease_history id    DEFAULT     �   ALTER TABLE ONLY public.user_disease_history ALTER COLUMN id SET DEFAULT nextval('public.user_disease_history_id_seq'::regclass);
 F   ALTER TABLE public.user_disease_history ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227            A          0    17121    chatbot_patterns 
   TABLE DATA           F   COPY public.chatbot_patterns (id, pattern, pattern_group) FROM stdin;
    public          postgres    false    214   �L       C          0    17127    chatbot_responses 
   TABLE DATA           I   COPY public.chatbot_responses (id, response, response_group) FROM stdin;
    public          postgres    false    216   N       E          0    17133    choroby 
   TABLE DATA           6   COPY public.choroby (id_choroba, choroba) FROM stdin;
    public          postgres    false    218   �Q       F          0    17138    localization 
   TABLE DATA           _   COPY public.localization (id_loc, woj, miasto, choroba_id, session_token, created) FROM stdin;
    public          postgres    false    219   }T       H          0    17144    objawy 
   TABLE DATA           3   COPY public.objawy (id_objawy, objawy) FROM stdin;
    public          postgres    false    221   U       I          0    17149    objawy_to_choroba 
   TABLE DATA           B   COPY public.objawy_to_choroba (id_objawu, id_choroby) FROM stdin;
    public          postgres    false    222   &]       J          0    17152    patterns_responses 
   TABLE DATA           E   COPY public.patterns_responses (pattern_id, response_id) FROM stdin;
    public          postgres    false    223   _       K          0    17155    profToChoroba 
   TABLE DATA           H   COPY public."profToChoroba" (id_choroba, "Id_profilaktyka") FROM stdin;
    public          postgres    false    224   �_       L          0    17158    profilaktyka 
   TABLE DATA           =   COPY public.profilaktyka (id_prof, profilaktyka) FROM stdin;
    public          postgres    false    225   �`       M          0    17163    user 
   TABLE DATA           5   COPY public."user" (id, email, password) FROM stdin;
    public          postgres    false    226   ߘ       N          0    17168    user_disease_history 
   TABLE DATA           k   COPY public.user_disease_history (id, user_id, user_symptoms, disease_id, created, confidence) FROM stdin;
    public          postgres    false    227   ��       ]           0    0    chatbot_patterns_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.chatbot_patterns_id_seq', 38, true);
          public          postgres    false    215            ^           0    0    chatbot_responses_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.chatbot_responses_id_seq', 36, true);
          public          postgres    false    217            _           0    0    localization_id_loc_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.localization_id_loc_seq', 3, true);
          public          postgres    false    220            `           0    0    user_disease_history_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.user_disease_history_id_seq', 1, false);
          public          postgres    false    228            a           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 2, true);
          public          postgres    false    229            �           2606    17180    choroby Choroby_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.choroby
    ADD CONSTRAINT "Choroby_pkey" PRIMARY KEY (id_choroba);
 @   ALTER TABLE ONLY public.choroby DROP CONSTRAINT "Choroby_pkey";
       public            postgres    false    218            �           2606    17182    objawy Objawy_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.objawy
    ADD CONSTRAINT "Objawy_pkey" PRIMARY KEY (id_objawy);
 >   ALTER TABLE ONLY public.objawy DROP CONSTRAINT "Objawy_pkey";
       public            postgres    false    221            �           2606    17184 &   chatbot_patterns chatbot_patterns_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.chatbot_patterns
    ADD CONSTRAINT chatbot_patterns_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.chatbot_patterns DROP CONSTRAINT chatbot_patterns_pkey;
       public            postgres    false    214            �           2606    17186 (   chatbot_responses chatbot_responses_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.chatbot_responses
    ADD CONSTRAINT chatbot_responses_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.chatbot_responses DROP CONSTRAINT chatbot_responses_pkey;
       public            postgres    false    216            �           2606    17188    localization localization_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.localization
    ADD CONSTRAINT localization_pkey PRIMARY KEY (id_loc);
 H   ALTER TABLE ONLY public.localization DROP CONSTRAINT localization_pkey;
       public            postgres    false    219            �           2606    17190    profilaktyka profilaktyka_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.profilaktyka
    ADD CONSTRAINT profilaktyka_pkey PRIMARY KEY (id_prof);
 H   ALTER TABLE ONLY public.profilaktyka DROP CONSTRAINT profilaktyka_pkey;
       public            postgres    false    225            �           2606    17192 .   user_disease_history user_disease_history_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.user_disease_history
    ADD CONSTRAINT user_disease_history_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.user_disease_history DROP CONSTRAINT user_disease_history_pkey;
       public            postgres    false    227            �           2606    17194    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    226            �           2606    17196    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    226            �           2606    17197    objawy_to_choroba fk_choroba    FK CONSTRAINT     �   ALTER TABLE ONLY public.objawy_to_choroba
    ADD CONSTRAINT fk_choroba FOREIGN KEY (id_choroby) REFERENCES public.choroby(id_choroba);
 F   ALTER TABLE ONLY public.objawy_to_choroba DROP CONSTRAINT fk_choroba;
       public          postgres    false    222    3229    218            �           2606    17202    profToChoroba fk_choroba    FK CONSTRAINT     �   ALTER TABLE ONLY public."profToChoroba"
    ADD CONSTRAINT fk_choroba FOREIGN KEY (id_choroba) REFERENCES public.choroby(id_choroba);
 D   ALTER TABLE ONLY public."profToChoroba" DROP CONSTRAINT fk_choroba;
       public          postgres    false    3229    224    218            �           2606    17207    objawy_to_choroba fk_objawu    FK CONSTRAINT     �   ALTER TABLE ONLY public.objawy_to_choroba
    ADD CONSTRAINT fk_objawu FOREIGN KEY (id_objawu) REFERENCES public.objawy(id_objawy);
 E   ALTER TABLE ONLY public.objawy_to_choroba DROP CONSTRAINT fk_objawu;
       public          postgres    false    222    221    3233            �           2606    17212    profToChoroba fk_profilaktyka    FK CONSTRAINT     �   ALTER TABLE ONLY public."profToChoroba"
    ADD CONSTRAINT fk_profilaktyka FOREIGN KEY ("Id_profilaktyka") REFERENCES public.profilaktyka(id_prof);
 I   ALTER TABLE ONLY public."profToChoroba" DROP CONSTRAINT fk_profilaktyka;
       public          postgres    false    3235    224    225            �           2606    17217 )   localization localization_choroba_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.localization
    ADD CONSTRAINT localization_choroba_id_fkey FOREIGN KEY (choroba_id) REFERENCES public.choroby(id_choroba);
 S   ALTER TABLE ONLY public.localization DROP CONSTRAINT localization_choroba_id_fkey;
       public          postgres    false    219    3229    218            �           2606    17222 5   patterns_responses patterns_responses_pattern_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.patterns_responses
    ADD CONSTRAINT patterns_responses_pattern_id_fkey FOREIGN KEY (pattern_id) REFERENCES public.chatbot_patterns(id);
 _   ALTER TABLE ONLY public.patterns_responses DROP CONSTRAINT patterns_responses_pattern_id_fkey;
       public          postgres    false    214    3225    223            �           2606    17227 6   patterns_responses patterns_responses_response_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.patterns_responses
    ADD CONSTRAINT patterns_responses_response_id_fkey FOREIGN KEY (response_id) REFERENCES public.chatbot_responses(id);
 `   ALTER TABLE ONLY public.patterns_responses DROP CONSTRAINT patterns_responses_response_id_fkey;
       public          postgres    false    216    3227    223            �           2606    17232 9   user_disease_history user_disease_history_disease_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_disease_history
    ADD CONSTRAINT user_disease_history_disease_id_fkey FOREIGN KEY (disease_id) REFERENCES public.choroby(id_choroba);
 c   ALTER TABLE ONLY public.user_disease_history DROP CONSTRAINT user_disease_history_disease_id_fkey;
       public          postgres    false    227    218    3229            �           2606    17237 6   user_disease_history user_disease_history_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_disease_history
    ADD CONSTRAINT user_disease_history_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);
 `   ALTER TABLE ONLY public.user_disease_history DROP CONSTRAINT user_disease_history_user_id_fkey;
       public          postgres    false    227    226    3239            A   �  x�e��j�0��������Or
49��=r)��5��-ϲr0ֹ�gX�=z��^�l�6lNf���g�pO�T�)J�KaT��	F�C��ՠ���Uš^ÝU4���}��N�ܫP\��VIK�Bxe�YGQ���*�'ܣ�|�?�?�
�X�&��Yy+�C��E�{iY�Xs^S�V�bv��Vt!��k�2<y���&@�S?��b�g*jJ;�j��ǧ�k�]��I`��$M����r
�J��LC������*�Vh%r�ÙKj�W0��h��q=�"��5<)���-��v�=����ѵ�v�)�� �Y�mT��R�k�F�(]��4�۽���9��w{�Ǿ�DN���H<�t��ZE���_��ٸg��[w��t�w]����\fa���X���0��Q7sK���L����(��6�!      C     x�}T�n�0<S_��� ��<N�� Is�K������uE	�T�b4�7��\s��_��%�q�����,9�m�b鬩��))Ea%&��X��f&5���Xd��2�����Z����9�b�6�ﶅ�8���JMaZ��c��R��?7J��4��8'YX]g�����y�~NiU�LaYA��f2��*�ߞ�+[�H�%�Oq�!�f�����H���H\�5Q�("�͔��`8Sk|���_�Q�Lҹ�A��-L��*��K�[AG���n"��q�E�g�&Qe�}�?bw�X\���;Ah���2Sh�H9_�4��kt�}f0�Ҕ Y_�^�T��?~ɔL8�*,��0&��9bZ�Sg�ҠE"����݅Q�l&��B
iv"�� Fb�&���,Uw��U��**0��-(^?�hF)��Vl���f�+�+�*\Dز��$��*^�����h�?�`e���@$�?qẗ́0`�^�龟�[BTXB����h���X�,G��Q�[�4��8�SU&��>��@���-���\0���uͽ{�����l��Nq��,�-���X��k��+�|ܷ�[5�.���ƾ��2g��2D�u��c`�Qˣ*�!6[׎3���xUֿX��&Tо��W��5;2�o�m�le�����������w���1�`�9o����Q��(���#1�EV�+vo����}�@�(�H$��r���S[��q�����cխ�*y�k��XL��&?������k�h1g��6�z�A�^/I�      E   �  x�mTKn�0]���ZX_�K;ik4�@ٌ%�f$�IA �F����1�+��u��n��8o�#�{o��X�O���o��ʺ�KGc�0������j�|�^�hJ�|�<�#nU�u#��daU�z�<�Ps)83�a���%���=��X-Ys�����]zDU�-��~�UŶwt�zִ���yE�	V� �+Exh�%���9&K�7�������հC<��Н	�F)Y;%E�猬���Kǜ,�*����jN�)��<T�F4C�ƫP1|����w4�bk��Ɠ3�W
�A$:#��o�hƺ����lE����E�U'���$֦g�t%���r��Y|�-�3z/xYcݔ|�^���j��J�C���$��?f�K��/2�����dF�.\��|�w��	MpV�u`�&�xF��Q�K/P���N���\s�A(#�B��Y=����,U��)���`
�F������wDL���<��w��kî+h]��kӘ|<�,|��4!_��l��LӔ�x���3�-�G�)9��4���B+=H�N�M�,r�&g�þft:�a�_���g܍��sr�����&����������'ئYDn�%R�sf1��%0�[�@B�WxN�=����X�x7�G�����:�#�G�����t��4��@�kg;��_�	�����%
��O!"�l��b�H+oHN�|���(��[J�>��M      F   �   x��̻�0 ��7E�e�'vnj� R@� �����"�����x�����i,V]���nvy�O��u��n�KR��M�FR\���Ԇ$pC*�oX+����F�+~�P��X)�,�����7�1H      H     x�mW˒�8\K_��0�v̾{=����C�@A��bn�7T�gԮ�ve����vݹ+�::�'O�?�)ZՉU��Z���Y#�U��<f��K=6bM+�R�A+;j3�O08�q-���r�T��S�o7����b^F}{m0��ب�~��{+zYv�<�3ֻ*L�9��N�i�g?[�U�Ϣ���y�с5��*'�Ĩl)y�����f�X�ytd�f]�{И���*�3R���>��N_�n�Zh1Nr�|�y����F�AM��x�3�R����簌��すq���-�,WC��=�h]S��[����.bl>���O��{usd+���o�o��Ĭ��j4���*Ǆ׷�E�u�a$e#�!��@<K�1D�i�)�׿D#m��1c��� W;�@�V�>Z=�iغ0�����B�l����)��] ����ƪo��b�R�Z�#�L����G��ښ���l��-	b�p���	3H�����Z�i4��;2k��t���I��i�����s����Mtr\D���X� ��O9�q���3Y�q���VV!KVɁ�� �g�#y�� �&f����yrd��$�$�����I9��o��Y�x���Z�$̺��E�uta�b-��W���p��kÓ�-d�h��dXl������`d�,��zǓ3���J]4�/U������NS���`ݞ�4B5�J��h\q҄?ᩞ�F��� s��:b�$��Z�&�M�MH"=M<���l*���]�nzb�y�{}�I*� O3�{��F�T�K�hZ��4�y&F-'�?�d)�i��j���p������Ȓ�:��0�P3vƖ��y�=�'*��VOu�1?ŬR�"�)�҂���2�L,5i��l�(u���3V ƨ}I#y=�Ξ�-����f4���,���K��˶������j����*hǳ#��Pl u���$2��n�r����ESHXaZ5�$er�} d��|/�I($W���ל@�urqq�7�e̕�O<;�c8��c���;πfgZ=��ɴP�^\伈 C;G���ĒNa�qn��P����> ��m��3���	����>|�[Y���W��]��	x����,ꠕ��t,���g��3(��]��Z��Y�$ϩ��f�Cj���k���>�sĶQ��7$&tHQ;�1?���MZ.���^����z��Oās�(��M���sB����&��u���2�U�ϧ��l*HhO��� :Ї"��g�(Sz%�����O�7#��%��`i�0*t� w>u�+Lc��������z�I��6�+E�B�{�i|��7$/�-����;WI����!�~�l��X�FE��;.�m�{P��{*=�Uq��(�vhݺ��Vg��/��@x��Лp1�0D��AD�ͤ�*��9�w6���)rv��ܤ�T`�(�*x̊n���aj�N�X0�ͣ�#x��5|Hn����{Ux`�*[�0���=��@���U@��0���$��	����P��+��{�=A#x;��\e8�W�
BO���:H�y;9+p&D/�:�|�/�$�,&9�C^��+��d��O"�\/�2��$�Cp^�!Á;�`�X��q����8<c�y��_xD7ٺ��K���#������T�����3ԯ�f����#��fx����K8����1�E��F'��3�Y<%�a'#xC������}H��)T�{^)�OfA�����q�8r���#:���{K���$|���%���*cP��w�����np��]�&�"�򌳶��I��@~I�|]z��/zI[S���F��wUO2 �8/�|��V����S6�heu�	9[o�P nj3`w�w�c'�=A��@�S"J�t�+�@�D�Y秦��ے�|�}qP�1�Zz�dw�򩔻�T]z|�ŗ��k�B�C�I(�R�P2��~�M��7�y�50���f�Ǣ��>�X�C_"c9�>��3��Q���?��9�4q��      I   �  x�5�Q�� �oY̜ �����:����ȭ��Ƀ��-VX�(���vp\��?�$H�m�I�&�\2�W��o�����d��~,�d@~�Z:�5�I6��e�C��qʗ E��\�,߶?�2dʽ�l�ly�Cs��%����^���X���Z�Z#�:^�/�������­C���N�命?���Ѓ;�?��e'�%1���`�cg��$�v�ϱ�+񕷬�n�%J#�^9tP����m��%�"��18��ʦ�i�`����*���\��4�������ׂ�Q��7�k3X�(,� �q�N�o�~SӞx��^��wc�߼8
t��9�i����7k��]P��0r��ר�x�7t_�|�Ż�$z�؞������S�����v�"�Ea�h�a�hE3���f�SCG�4�nQ�����"8�@��s�	ly$:�~���!*�@      J   �   x�ѻq�0Q�F��AD.�?5��),�������e63L3�$��$�x�'�x�^x�^x�7�x�7�x�>���>���o|����7�q&��/q�!��n�w�s��v��]�㑋�"�G�~�6�l��4锝�Sv�N�);m������v���;cg��n��2��5��՛i���h����*����ɹ=���W��U�*���Z��HKf      K   �   x��Iq1ߕ`]}I��qx�a�TR*Z�hX-G�����!�l�r���x��+/>��W��ɏe�V~��d)�le��r�K�!��O��Pe��T}��fQ�jjTC�j��:�U]�꠭6��K�5~�M�z�U/}ԇ��K?�cB�5fR�Li�i�w�[4�j�9��\�e�污�Z��M~�?��3�      L      x��}ˎ����)�i ��$�me�ƒz,ٖ,X���#Ȋd0Hxi�2
�fU��a0�5�Un�!�$�}�����f?�2"x�/�������C�[��,�/�}W4.kwK���׵|=gu��#~=��R����g�tW����v���1;uK�M�?m�_��[�ŝ�mY���iߝJ��ָ���Q/���������eΆ����C����u�q��j�c3o�����2����9�}���ΦlW��n?f�_`>�8dm���T�S�:y�&��"�qӾ�{��(���j��`(Y>>�X�f(�2�9�ΞR6�<��莸G'�v����~��Ôv���q��S����?Zk,Wמڦ��;�>�'�
�ޞ\7Ț��+W��~뇢k˼���=n���=ٕ������/���7��t�U��3>b>��;�;�6B�_->�*���SW���d�n<a���4��&�-�j)��k���X�Y��xr�=���6wy��<	I)ad���k����]�c���&[�c]�Oݼ�ON>��~���OeӴ�Wxόw�ڂ�6�l�&ۃ܈-���&�V`�E�\E�]nw$?�Q����1�g��0'S��N?��-�y�}�L��6�^���GP*�Wc��m�p43p�5$N�9`���C;�q&�W�|Y�O�����K��+��Ǻw�r��e�H��0��,�"�a=^��k��"I��w��M�kz,4�n���?<褼�6�6O<�Zb���]�lA��$�������w7~�i�sLTZ�a!w����W�Yg1W:e:�-d��7�u�𚻇��=���8�M���>|�+3}[v=n��&��ļ=�c9�e$��$L�4�m9�7���qg�&H����x}�"n2��@��eXނPߜ�_vC�6;lD7LjF�^F�v�O��_d=��L0����)y�k���Fn�l��z �5��_&��J�M�� ��t��� �!�r�?�m���.���\_��v��nq���}Մw�QX����n��֤&��7n�6,� ��R�|��û q�k�����H��~?��� �a�1{"�@�x��=��&��@�9إL����~��i��}����l�����G�}Ml��ۈ|�����1���jq۱�	�X���-�?O];�d��K����H�����)��f_+���-s,�X(m[��o�(K&�q^���I]�Q�@)�������{�Rd!{h���jjc\�K�,���C!��gQ���s�F|A�L��l}{�������w���{U]5�w�C'�b�M�0X�A�6�_Ȭ���6�TRU����� QsD.'�;�͊�4���5DZJ�y뉁������?� P����ZЇ7������g�T��%����d`7*�[v��9��6�RP��6^_���x(���|� PK�w�}�O�=?�i }��]���A���T������2�&�g��]���bC>�{	�0&�l��@�e�x��d��M�/J^��18n:$�/$��ĠO~�V���_Q�^%xTS� �ʌMYqZ���	�������xF(P����uQe��E��%�$�����~�r�п��UP|� ���,������%�@<
�'7`h�W���[<_� �aZ���q�@����U3�VM�K�7� @&�����#����_�W��U�9|�=c� )Ty��h�De�6U��-���?�u�$��w�vh��2
/2�Y��UG7��Ĉ}���u�d�U�9��dT��w�u֌u��c 4g}�Q�}�]�������^}�l=@��-u������E���ד9,��h�i:BG�V�x;�T�|�w��@�N�Hq�V����<�ڌo*#��qUG2�Iu$���Y�s�Iy7�K�o�n~��^�r[� ����U�M� B>2�i�X:� n�^��I�Ptuy��L���� N7���[R�+�����*���!�n (ػ�/U�x��2GZ�f�*s�r+_�B�8�I<�.v�����ȡ�bu�ىQ7e7��C���.�A	`��"���a� /�>@AC�ejy�(���曯ﲯڜc#��c�'<b|�s�0�p��mq����4@�ES �}�Ǿ(M�r��B��� }��EQ�4���)�ܳQ���8��TQ�Z|n�7�&���5�}j3j��	ހ �^��/����v̶�\��������N	@,�p�]���A}�	�:8��\�L� u��i�����j�Ϯ=�n�O0�����ե_r���x��m��v��[�����Tкv�{��H~{��@��O?,{h���EQ
��D�m��0�͚2�������:��[\�dQRq��Nfc���w����/݁���A��=�k�������͏=����3(["� 3��z�@�A��'�XS�A�v�d�b�E� ��(s�
@1�C1�3��حJ!�Xǖv8/9�9Me�oٴD��c��Hx��采ץ�.�����~�f�����Ƕ��d�u+n�L��A�  ���t���T��ff��[���"���EWT7���7)Q~�Ԍ����s���/���j���{�[�:诩�|D%f�@����-���J��<s�՛Ȥ��}�[���Z����Z���0�=� �� �k�DU� `���ށ����AX��y�NFm��޾�CĠ��E��N�x��������]�igf�K����O�އ���ȌLQ�9)K1t���9�?���i�y���Z�)�8w�[� Ҵ�>/�m����|5�!)< ~i�hNP��4���qO\�b�n�:N�i*|E+(a��ީ��i���{�.8>�j�L���S��`!��!w�>��@����k.
�t=�l2@I����:zN���B��b+ML$q\�L�M\PF�U]Q��b���꣟�l0 eOQ%�m�{>^�0��ojO�T+[�ۮ���IYD�ϥ�~u��w�eCWD��i�&Y�|�������$3Ht\�.��|�c�Q�$:w{GD�����8�NL�s�ݻ.��0�w_��w>��C{��W������R%�H�n-X�?���U��Lه������Wk�}��x�_!���d�;��*��%��6�O�Dt����q�,��#��j,}?�z���UJ2����{tIL++&x����/�Ŧ��BM�ET�D�]��{̀�����
{T�*���Y���H�`+/�����c�/�̈́PՕ�p+�ΪT=�{�ѡ]��5��@�v�x�j���\Н�|]�'Ν���+1J����� �̝��υ!�%�H+XV��
ܙ���C��˷�_f�=�׊XG������N  ��ǆ�!��b���'.���$9�S=D��h
�"���T<���=41��p�o�ZuJ�7�o�"�N6��]v��J� ��1HU^dc�@- �ަ���w[��*2�U%����Ɩ��,�త�9,�Q�$���$PQyhd���׶��.H�sF�/d
N�hݤ�������������_�Ӛ�0�16V^�K���<��@Aޏ�x<J�,Σ��;�E��j3�/k!�SOu+%+*65h�[�6�+-�BF?����Tʆ���Es��P6�`�N+��t�{��H��0;�-��I�����~wC�#BF�L7�Bt�CW�/��p�Tu+?�9E��/���i��TJ͉�ꠡ8���c��&�j7hU�x��C뉋���J�>��@{Z�g!�e����Ӯ�Hy2��G�Q���x�Yk{�K�8N�]���D�$�<��e�`ڬgUu1�)�n�1U���Q�$L�c4��R'؄z�z���`# #ܝ:m�}O`�Q���}r/�N�gY@�w��������.�@������|�8a����S��i��z�KQ�r��jOj�Q"x��^�N�B�P#b���0̧9V},"k��P��(�˄[l�i�L�-�H;@�/��y�De�D    e�E�34�G`�Ch\|��b���L����aa��YySY���;�;e�LJt{`d����X�f�SS�4,a#6��1���h�T?�S�a�a߭�5u�����5=f���\���<�'����K�/G���1�t��\�b� L���w���������
��鲌�nd���p7��r��:�S�s7��� Tb�KmLh��Cc���o	F7�/y9�I,��)�Z���'4�)z�Y��I1��/Uk�1N��<u�����1��դ�-ᗽ��kI/(5�
P"ZL��r��z���I��.����;)3'(#�D�C/���6��؉��X!�,�/Ås"�g��XV.��Ӆ;�1�`L�S���i�a�YW��:�;�)N�wGf#M���f@*ۋ��� ��I5�*E�PQ�o�T�L�,���r�_����{�ߗu;�w��B#��{�#4�`╵-��%ОR,��{Z����H�4�F��N��Q������3?ʄc��p�6�u��lo]Q�� -�<^P��	��q�'ȞN �X��(F/�dnE�>Q��!n��$������!X�DU����uF4��A�J_��~Wd�X-,��'�q��d\s���V��؂D�?� uA�*^A�1�|q��r��d["�Fë!r9�0���O�Bל�hfAx��gȨ�����τ�!B/Q%0��
����6���n�a.,\�3�o�Y������%jX���H^(�0�J�YJEi~�du*�G��ZF�n�҈5@� P!�w�i�;@ġ���{[
i�R3H��[4#x�BP����f?@-���^�-% �&�M<���_�}L&���W��>=��K�P�A>��a�g7�x��R�~�(�=��Ja;h�F�=����@����ؗ6��q㒰�$�u���=��X8W�ۢq�+R ǥ=�yEQ�k��Q .dG�Y)@���U�N
�5�I���;�������DI+��� W��$��oq�^�C*��@��3+0*:s7�@��TZB������{P<��5��48�����Y���;�ZCG
���{��3��#FO�!��~l��7&i��[��*�2M�H�W5�a��Գ9�>�q����Ă`���S�R�ԉ�%"�b�~�13��g��"ڶh��jL�̞?{��٘��%�k18Z�T=�\�I!)�'�')o�U����4��JH\3I,ؠ.bH�9y/��	܌�7�e��)�!��	��GG�iI��;
'�F�j���Rf��B���w:�1�4Ƕ�G�UW��޽+N�Qa�<��:�s���ZF�L���!�	,��H24$�Vx��^/fF^��'��.��8u@SW*���e�pR�����Z�&M��~�~���+D*�KI����`���k�ޒ����~�0�R���b���,ùxE\�\��?Ҏ�Q8ީ���f�Q=�岶�CJHb�;.d�4jέF�䉠�3�${2qY��\O��u��uҽ�J��f޽�K��3�]�h�/�n49#MC�	VjbP��l�Q�Z�xf5��I�-#�$\2H��c��	""+���	�Vk.[x�]��2�H���I�O�R��:L����%*=ڿ��ϮC��&K򪡈�r%P�̋��k$ɺt]�Y6z�Z��b�\��#,��rd~sİ�5paؒ8�.MXm���hF��3���i�s �XGG�{�2kx�Փ��<�t)�?�7`��.���O�L�#$�bXk�&rQZ����O��_����m>�0���'�^�Ƿor�ɴ���:@�ʖL]	3�a ��pN6Tx^���4��y��]/Sn���7[j�e��#�r��Xt	�Ґ��a��42kA���@�O���R��R�ʚM�L�UU
��A��r� *$��D�ek��Fʿ�Br�Y)��S�k��.$�%&�NM+��춉���/��������&�p�2�A\�DN2]FE�����Vw�Z@����[��^*�P.��ю�X��@+S�h?6F�ׅ��i>���, �v���0��48����2���ĕ�2�GW+�&4d_3O�q>TQGg����}.,�4m@���^��ƽl����i֕���T�U|G����bmDs<�\I�I��`�ͬd���A�I���>�#<&|A��Cy���j�YK�(��/!�K���n֩�U."p����ͣ�踚-1S|����d-#��G�Ŗe#K�qͬ暸�v�p5q�_����}>���a5:�I�9M������u\t��XL�����*/k�h��А��1��hD�ΉQg��>�V���x��p��	l��cF���2;1n�	�y��?Dn��a�z[���B�'5�]���w�03�X>���,��z�~���1-�O��g���B�њ΁��W]`w Oh'���h����6�-��$�XO�:ј��(}	;�eJ�
z�)2&Xf/������Y�����N숟K�IV�7h��'".����8��٫���i�V�v~%�i'K:�Rd��
�kꉾ%E)��HG�{p?
[{�,e��hF����Yǘ��\}��T��&��=U[� zUXv�|��ܲ�Ȳ[�-�|��%:����@�|����hH�
>�-��N�Y`�y�B�лk��m ��RCV��a�d�I��ڧqS>r�\�6��l�e
���'���6t�֗����/��f�: ��șMh1E�sI.�ѭ]	�=�I�G 9���L��΋Q�}n ��c��y���l�I��G8�=|S�T����`�'Ȭ����OPW��Y�s�Yf����㈐Id)�Q��ӆ�$���
rҢ}�Wxr��[5�!�|��j$fI��fLk��)��U~�e ��bR6�xdP�o�B��5��I��Ḯ ���g��DT%����hd��ے�Z;k��^L�>�'I�8�ION�W$��O�s���>��I���HƊ���Ұb�]y�@+�F=�Z���H.���g�3Tg�p橄�{� ��k�a4��{",ɕE}C�Q�[�/����s�7�-D�ۆ��&��]��2|(0�pնl�/��/��'����5�9� Y�҃�蔝�$(Ճ��sjY��A��+
&�5\׷e�=i����C��af���I�fU���� �>_Y	�x��.�?�L�����#�U���:JM�,I���	��xD�e�����B�[��eBoe49Rb�@V$���i�2ݻE�ˤ����`eղ֖E/.ۭ&D�j�5(���%>J���\4!�����8q�J�i:�C��Vj��ƢM0��d�;�?����$:��b:�j�:�߲l1�-R٢�@)��#)�D��u��P~A������9-�Y����e�8cS�]�Z:���|�=��8avX\���<�áJJ�.7V��h]��I=�ϠήŎ)mJ�J�	ek �P���YϝK3�w��%<�ߘ�oZ1�u�w�$�K�!Րi!iq������Q���<��=�U�#��[��niO�0��X���p�Ua�`Y�~��R�ɤ�b�`S����+s�9m���Q%��ܩ��35ѫ	/��]��$q#����T�rLEǸ�;��#�Jq�>�a����>�?�p��3�\�w�9IC"f%�e&s	Jf�۵�A��w-{y�N�W��B�I��Ӣٻ;F�C!j{V1ei���VE�_D_!̒}Ѵ�������%��,W�.�]ܺe��<�^*����cLJH����e�{.�R����1�`�u�07��7ʋ�G�ڛO5�ÕY1�<��JZL��2~����Q+��l�u���;F��Q�Y���U��!!�C`���z�P��Z`��[s��`�ڈe)�.i���\�s��K"j��*A;�N����B����ss�}.A�����Xl�T���I�enp0�Ӧ�%�@6ѶR!(¦����I�����޻Ɉ��38�M���G�_zm�.C�$o�����4��(�̅��zv�q=��^��-�^��� ѿ�V�I�x����Ηb �}1��    �ڴא��?���������g�ӌ���r�
C\�8C��ߝ!�i�0e�pk���l�ބ�]�p���r��~��˪��2i��jU"~ r�醎>y+ɤ�O�Ѽ�P�pR���������j�M�m42�2����V���t$��[�1����(4  ] ����+��������j+3*/0�̪C��.#И���̣��i�ad�B���?���~�P�Ջk*��Լ=t�,&�]6 #�y��B�{�u�%ڗ@M��<��dd�]�WLq0eo}5���q���S�k�5���}$��Ĥ�ص>�����H�|�\X
�`��m7>�'����f͍����}E|��|���N��{{�c�jQ�9S94�'��z�O2<r�=�o�+)�e���G�e�̜� WP�ؗ�E�PZm��Hr&s�$�uV�e�|�-.�>K�\a�US��w ��N��4iR�����;� .�ؗ�J�<_��Z�5���K��I�<���2a?(���W��P� ��~�d�ߎ����SsP�8����*���`�Cu�֯b���.J̋�2y�db��W��IS�ې/�Q��u�;��!q3�
q�ZA��G)7@��e�5��`zHL3����}��J.-�B3X�5<��^�1���j!->�'Ƶy�W��������<��G�n�/���W�(ߔ��Zv�K���m��_O�G+d��w�3ޤַ���_ߪ�E��t&��mܭ�V��E�}=eG�i��#U�-���7� �<��X�l�I�؉�,2�4:������Iۤ�\ds�V5����C�7]�0n�� �J�r�k�c~��ї7��ğ}��Ɓ��/O�����=�K�fs�ck��y<��vU1�7��۴���$��3�d�|������sY<�w�;��+�KY�]{}�"F�o?��T�X�Vq�m�/Tez�@R�kV>�^:oN7�܉(H^�`��4S0����Eq��T]�/&�Zjj��j{�8�u�V��uI���IZ|b-��
�i�6�:�6��0��8����(���`lZ����g�7+���;��ۦ�����jMj��`uZ������}�a[�������|찀U��nd4�����~����g�@�[塞�Ԧ^R�f�',�M�e���8I�b��Z�b�����՟��J�n��_�$9���2U<�� ��գ�$�z�aH����e��{�<��^��^i����Τ�az�4a��:G�d)%Z#惮I0wq���-�ć!f�{ZK�>Nj�����j�AN� �A��dB��fGm =៣v�x�FC��]_��x9a�~���^G��ao�S�\�zK������<��w3ے=4	�K�r�$��:��ﺴ?M>�q��)s���+l��W�6��W��t!^��a��{�֒�z���Hl����ln�UX�'���a"\#�Y>��v��.��Y�:�5/m���ee�N|�:gz,~���#�(�v�NR�8���5� �b�;�8��9tt��7PX�txs���]��Ƴ6��s�f��P
�n;I���S�	��].��+����D�)2��^?�z#�����M�5j��\-z-s���z9:�A;{Q�>IM�ɸ�����ە�)uʧ�y��K�t�P
Y&!����f�}�WH�w%@R�/I�c�Vߣ�8&5�E��댤X�|5G�~�-�C�:N$B���,���HJCm�]I�����ǹk���✸�?��_o}}�w;K�*�:�"�ЂC�F�L����2b��O,�+ёA��ڭ��z�]YIl�#YF���)�_ؙ�[f��_X��n�[�#�� Y�cj��_��O���ڥ���rż6��n����|�z^���X>K�1��3����?_qz!��gİ��rpR���[*�{z�oÝb>[$ȧx�u���F�%�-$�b��-w\B�X
C�!����;-aY�a��p��'5��s�H2���$	�]7��D0)`&XLX�4�CRҊJ�$�2ؚ�~�d�"�rҗ�KY���Y���l�R����\�}U@s��sΤI��=Ce&7ѾW^���%l��m��hѓ�I?˳�z܎ ���}�6r�zs�)җR��ݳ�����/�q�Xe
����$��������2�F�W?�����l�4�Ew "��:�E���р>�W^I��^{K�9� J���K�����b�n�bMֆ��i�0ajl����߭'v�}#ZS��b��X��(1�<�*�!Nu�tHJ���:�K?Mƙ�ۤ�b�ֵ��B�q�_L
/[/��
>־�jXT]y��6I�sښ���$\�{X�ؘ��|�{��cH0���뙀)�G�3+I�{�R�-��4������"�a�5VC+����z
�Ur�U@%ݧ�(.I��9�j"շ~)�xU�-!�ԔAᘲ�(��������^���{�I���R��%D4����m���7:��i���2�<o���av���n���N���?��>JF:W��KG�*�zf�Jr|ԄJ�w��w'J�̠�1��v������tׁ����=�T�L�k\�#d��q�%`_���ߪ�T�a�G��@��[�t��'}9H.����x�;i�'K�`��R��Xd��t�p�j7�d̛�S��ʸ,��~όe�m�\]ϋ��B;Jk�ر�Q�О��C�~1����һ����7J���$���?��rp���I�qŌXe}	U��SA�,�}B�I����#�3}$Z%�e�3�Nb��3�]��zHV���0�&�܄c��ޘ.�uR���c�`f_IDkՒ˖��ia�@&SAes���.��XTj����㄁�8q4��ԕ��%�A�K8@�vų^��p_�J{f��u��R��~�R�H`-Y�)�҆x��_u۝����'�t���Q�g�Yi3kŷ� ��6������c�b��{a�^��߶�q��w��Y��ȧ����p�����U������J+�bKbGU��'��N|b��8��y��"<8I�!K�Jb�3EM�o�cmR�����J�~���U ���BW#+�W�ȃ���E�1m�QcXR'��V�^>*�gg���5��R�9�~-����ZZ>f�^d�?sd���nE��}l0ש�`Ž����(�a�5����\�H�)_��j��Y��;����Bn����A�nD�|��x�J81��(�����FB�f�����O�H\Uv��P��H�GC�wv��u�8�I���cP]'+��k�h/��Xl/3K��Ɣ�Xؽv?i	��P���[�0,�c�
֬yA6�b��A}��-�D\;c��g����6rz���u�� ;?'2�	�����jK�f�[��	���K��YK�\��A�C�I��|_;�D#�LܡCF��ف_#��x����J|>�l�2�=*��s*���j
f:���.V���|�G�!���˾5о6�B&C1�C/��:��*]?�aQ�V�����nHy�F��%���n�g��a�RְF�>��-���_.d�\�'t�\��,F�E'��WU�]׸�Q����؋VO���h�?N���*P�;��&�.���Vg��!���r�"q�da���;+��uD)b%��<K!}�Q�9��q�C��[�?��1�=q�/H�|��O��}^~J�tz��Gy��}񧂽���C��Eσޝ��!��f�l��L�/����x^��o��""[�]n�O��{>��=����!����$����VR��T:����$�<N���0�Yc��R��O͎��o@��
��="ы�`��@e���J�E�L �) �^/�qֆش�%��9+���<����T�146��9p&��+W\2�鐨R`RSo����6�4s�E�*;z�rZ�_ʳ��`�')�$h�2[ʖ�K�x��[6�'�T��Q[zo�b��O=�W;��^���R� %oSΪ�鰱^̚WʽH����Ѷ��%����;;!PV�B�ݬ}����C���.	�U)�Q`�sqkV��-�вo��n�e5�����>�Y�ЊU�ьFt�<-R���'��N�o�?|�H���   �A-Z�j��]=��t}�o�D5���?�u;�~��9���VY5���g��T�$^�r]9uz_4�Ջ$��I�M���i��!�ђ�h/�D�G���ݭ�70 n�T��Ug���W_��C����9E��c��6����&��,�I��q
�.�BE�4�9��H�O9�ٰU�a�����r�w����ױ�ϾaI?�VQ��NS^�NXe��"��+����KHK���i�7I��C8�#`���`*rU�ˊ��Z�Kxۗ����!]vj*Č�!���\3��z��SLX�yȨǓ������0����V�nDC0��iy,k�u�XS�x= ʬv2l�T~ُx�Vӓ�b'1K��hv��,�ڟ�'��Z}|)�0m�r6�2�e*��L��C�=������S�ٟ�.hՄ�CRV���=��2p=�H��tb'�H��!M�*�tXC��(i��ڳ�j�Vް�G1t���u�a�Uz���5����`�3���^�V��[���~�~f�)�1Ҧ�X��&���i�4���� k��K�/�@��:��c�uT�{��<�jVU�����������xd�۪,Z��m��]�Tv�C{�^�UT
�}��/�^ad�E��ب�g��K/�������S��Q��+h\�gZ�q,����Z�i(J����5!&
�Y����"j������&�G�%�Rk�_�T���6xЬM�yJ��Nٚ%t�[㳎�aqC�@5�R�r��,��ѥ�H����5Ov�(ʺ[=������ʎ��IƳ�B��pE�27l���@�q�I~k�A*��Gb��VyV��rEm �_�əQ��n}��冟�r�s�AH�F�#�d�]VzNf��F|��Us�P�*��袲�c�qծH�]��t�/���>+2��,"��^A�D|�"� �["�!}�]���=~s<��\����h�0�kD�C
����vC'V��B��]��RҶO$�&�V�W���BB�<#�J�.՚kZ[��/'An��ڟ_,�$/<�&���9Uv���1>�9$ ��%[:%�]ϰ���ךI�2%��������
�I�$#�d��l��KL��7��,��`�{���ׂ�|�ӱ�ԣ�̒��H�e�xm�U��k
G|�z�3�O\��Q��x�I�4��:y�Y�����TD�LV{i���	(�J�^K%f�c�$=aE��Dp'u:��ao;"e�7����&f�h�c�ت�ɵfP\>$o%�n�T���c��(�#WL�aaH$��!�/`��`r�#=��ǘT+�?�,Lm߇UIm��t�vN�cB��):�Q۪��^,�E��h��+nBwvr:�����.�mH"�}�Q��iG��w�㺌����%�s� V��Ϻ!�EJ�[M���	I�����$�>8S;K�M)�i�3IƎ
�M�5!X4�uh�]n�y9rmw?�����(����k߃���K�\�_�Ǣw���9��ߗw_%ы����͍����\�*��G!\F&�c1a\ՕV)�E�g�ۮ }���������=ψ����'_ߘ��4�]������u��/}M,�T��a�D{D1$]���c��)U�,��h���U��=d�_�kK�o��V���]��L�E��>��ϲ��i�磥2��s�)E�tf��YK�mٞ$�~���0�D�����w_�^�!�V���%�m�PY��c�
���NJ���
�M�==M���w*��¤6��2��*��C�s	���GK����v�l�C"{4����M�\�4�>9���_��Y�"�'r�/�oB҉�[�����R�G�IMWS��Eh�D�l�~A�����U��t+����.�y��Z������Z<
t%��X�DlB^j�wAW�88ǅ�oS��|�4Nky$5��J(\��������>�:hƘ�Nj��-����S��es���7d7��[�C�w֚㶤VA��obB�?���s�d�ʤ��e��.�����,[��os��V56��H���y~o|�aä�Bl �Y�3��~�=��`�e�W��^]]�_�|��      M      x������ � �      N      x������ � �     