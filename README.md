]]# Apache Superset - Guia de Instalação Local com Docker

Este guia ajuda a configurar e executar o Apache Superset localmente usando Docker. Este setup é ideal para desenvolvimento e testes, mas não é recomendado para produção.

## 📋 Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) (versão 20.10 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão 2.0 ou superior)
- [Git](https://git-scm.com/downloads)

### Verificar Instalação

```bash
docker --version
docker compose version
git --version
```

## 🚀 Instalação

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/app-s4erp/superset.git
cd superset
```

### Passo 2: Escolher a Versão

Use a versão estável mais recente (5.0.0):

```bash
git checkout tags/5.0.0
```

### Passo 3: Iniciar o Superset

```bash
docker compose -f docker-compose-image-tag.yml up
```

⏳ **Aguarde**: O primeiro início pode levar alguns minutos, pois o Docker irá:
- Baixar as imagens necessárias
- Configurar o banco de dados
- Carregar dados de exemplo

Quando você ver mensagens como "Superset is running" ou "Booting worker", significa que está pronto!

## 🔐 Acesso ao Superset

1. Abra seu navegador e acesse: **http://localhost:8088**

2. Faça login com as credenciais padrão:
   - **Usuário**: `admin`
   - **Senha**: `admin`

## 🎉 Pronto! Agora você pode:

- Explorar os dashboards de exemplo
- Conectar suas próprias fontes de dados
- Criar visualizações e dashboards personalizados

## 🛠️ Comandos Úteis

### Visualizar Logs

Para acompanhar o que está acontecendo:

```bash
docker compose -f docker-compose-image-tag.yml logs -f
```

Para ver logs de um serviço específico:

```bash
docker compose -f docker-compose-image-tag.yml logs -f superset
```

### Parar o Superset

Para parar os containers mantendo os dados:

```bash
docker compose -f docker-compose-image-tag.yml stop
```

### Reiniciar o Superset

```bash
docker compose -f docker-compose-image-tag.yml start
```

### Desligar Completamente

Para parar e remover os containers:

```bash
docker compose -f docker-compose-image-tag.yml down
```

⚠️ **Atenção**: Este comando preserva os dados. Use `stop` ao invés de `down` se quiser apenas pausar temporariamente.

### Reiniciar do Zero (Apaga Todos os Dados)

Se quiser começar novamente com um ambiente limpo:

```bash
docker compose -f docker-compose-image-tag.yml down -v
docker compose -f docker-compose-image-tag.yml up
```

O parâmetro `-v` remove os volumes, apagando todos os dados persistidos.

## 📊 Estrutura dos Containers

O Docker Compose irá criar os seguintes serviços:

- **superset**: Aplicação principal
- **superset-init**: Inicialização e setup do banco
- **superset-worker**: Processamento de tarefas assíncronas
- **superset-worker-beat**: Agendador de tarefas
- **postgres**: Banco de dados PostgreSQL
- **redis**: Cache e fila de mensagens

## 🔧 Personalização

### Alterar a Porta

Se a porta 8088 já estiver em uso, você pode alterá-la editando o arquivo `docker-compose-image-tag.yml`:

```yaml
superset:
  ports:
    - "8080:8088"  # Mudar 8088 para a porta desejada
```

### Configurações Personalizadas

Crie um arquivo `docker/pythonpath_dev/superset_config.py` para personalizar:

```python
# Exemplo de configurações
ROW_LIMIT = 10000
SECRET_KEY = 'sua_chave_secreta_aqui'
```

## 📝 Dados e Persistência

Os dados do Superset são salvos em volumes Docker. Isso significa que:

- ✅ Seus dashboards e configurações são mantidos entre reinicializações
- ✅ Você pode usar `docker compose stop` e `start` sem perder dados
- ⚠️ Use `docker compose down -v` **apenas se quiser apagar tudo**

### Localização dos Dados

Os volumes ficam em:
- Linux/Mac: `/var/lib/docker/volumes/`
- Windows: `C:\ProgramData\docker\volumes\`

## 🐛 Problemas Comuns

### Erro: "port is already allocated"

A porta 8088 já está em uso. Soluções:
1. Pare o processo que está usando a porta
2. Ou mude a porta no docker-compose (veja seção Personalização)

### Erro: "services.superset-worker-beat.env_file.0 must be a string"

Seu Docker Compose está desatualizado. Atualize para versão 2.0 ou superior:

```bash
docker compose version
```

### Containers Reiniciando Constantemente

Verifique os logs para identificar o problema:

```bash
docker compose -f docker-compose-image-tag.yml logs
```

### Problemas de Memória

O Superset requer pelo menos 4GB de RAM. Verifique as configurações do Docker Desktop.

## 🔄 Próximos Passos

Agora que o Superset está rodando, você pode:

1. **Explorar os Exemplos**: Navegue pelos dashboards pré-carregados
2. **Conectar seu Banco Supabase**: 
   - Vá em Settings → Database Connections
   - Adicione uma nova conexão PostgreSQL
   - Use as credenciais do seu Supabase
3. **Criar Dashboards**: Comece a criar suas próprias visualizações
4. **Integrar com Vue.js**: Use o Superset Embedded SDK para incorporar dashboards

## 📚 Recursos Adicionais

- [Documentação Oficial](https://superset.apache.org/docs/intro)
- [API do Superset](https://superset.apache.org/docs/api)
- [Galeria de Visualizações](https://superset.apache.org/docs/creating-charts-dashboards/exploring-data)

## ⚠️ Importante para Produção

Este setup com Docker Compose é **apenas para desenvolvimento**. Para produção, considere:

- [Instalação em Kubernetes](https://superset.apache.org/docs/installation/running-on-kubernetes)
- Configuração de segurança adequada
- Backup regular dos dados
- Load balancing e alta disponibilidade

## 📞 Suporte

Em caso de problemas:
1. Consulte a [documentação oficial](https://superset.apache.org/docs/intro)
2. Verifique as [issues no GitHub](https://github.com/apache/superset/issues)
3. Acesse a [comunidade no Slack](https://join.slack.com/t/apache-superset/shared_invite/zt-1btuj4hco-57i6FmnCqN4DU1YTg2c9KQ)

---
