CREATE EXTERNAL TABLE IF NOT EXISTS `dengue_rj`.`tb_dengue_rj` (
  `tipo_de_notificacao` string,
  `agravo` string,
  `data_de_notificacao` date,
  `uf_da_notificacao` string,
  `municipio_da_notificacao` string,
  `unidade_de_saude` int,
  `data_dos_primeiros_sintomas` date,
  `ano_de_nascimento` string,
  `sexo` string,
  `gestante` string,
  `raca` string,
  `uf_de_residencia` int,
  `municipio_de_residencia` int,
  `pais_de_residencia` int,
  `data_da_investigacao` date,
  `febre` string,
  `mialgia` string,
  `cefaleia` string,
  `exantema` string,
  `vomito` string,
  `nausea` string,
  `dor_nas_costas` string,
  `conjuntivite` string,
  `artrite` string,
  `artralgia` string,
  `petequias` string,
  `leucopenia` string,
  `teste_do_laco` string,
  `dor_retro_orbital` string,
  `diabetes` string,
  `doenca_hematologica` string,
  `hepatopatia` string,
  `doenca_renal` string,
  `hipertensao` string,
  `ulcera_peptica` string,
  `doenca_autoimune` string,
  `hospitalizacao` string,
  `data_da_internacao` date,
  `data_do_obito` date
)
PARTITIONED BY (`anomesdia` varchar)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'field.delim' = ',',
  'serialization.format' = ','
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://health-data-insights-bucket/DengueRJ/'
TBLPROPERTIES (
  'classification' = 'csv',
  'write.compression' = 'SNAPPY',
  'skip.header.line.count' = '1'
);