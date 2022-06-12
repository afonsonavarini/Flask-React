import React, { useState, useEffect } from 'react'
import './App.css'

function App() {



  const [dados, setDados] = useState([{}])

  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [telefone, setTelefone] = useState("");
  const [endereco, setEndereco] = useState("");
  const [profissao, setProfissao] = useState("");

  const apagaDados = () => {
    setNome("")
    setEmail("")
    setTelefone("")
    setEndereco("")
    setProfissao("")
  }

  useEffect(() => {
    fetch("/clientes").then(
      res => res.json()
    ).then(
      dados => {
        setDados(dados)
        console.log(dados)
      }
    )


  }, [])


  return (
    <div>
      <div className='main-container'>
        <form method="POST" action="/enviar" encType='multipart/form-data'>
          <div className='blocks'>
            <h1 className='label-title'>Insira seus dados</h1>
            <label className='label-title'> Nome:
              <input id="input" class="Input-text" placeholder="Seu primeiro nome" type='text' value={nome} name="nome"
                onChange={(e) => setNome(e.target.value)} />
            </label>
          </div>
          <div className='blocks'>
            <label className='label-title'> Email:
              <input id="input" class="Input-text" placeholder="Seu email" value={email} name="email"
                onChange={(e) => setEmail(e.target.value)} />
            </label>
          </div>
          <div className='blocks'>
            <label className='label-title'> Telefone:
              <input id="input" class="Input-text" placeholder="Seu telefone" value={telefone} name="telefone"
                onChange={(e) => setTelefone(e.target.value)} />
            </label>
          </div>
          <div className='blocks'>
            <label className='label-title'> Endereço Completo:
              <input id="input" class="Input-text" placeholder="Seu endereço" value={endereco} name="endereco"
                onChange={(e) => setEndereco(e.target.value)} />
            </label>
          </div>
          <div className='blocks'>
            <label className='label-title'> Profissão:
              <input id="input" className="Input-text" placeholder="Sua profissão" value={profissao} name="profissao"
                onChange={(e) => setProfissao(e.target.value)} />
            </label>
          </div>
          <label className='label-title' id="curriculo-label">Seu currículo:
            <input className="input-curriculo" type="file" name="file" />
          </label>
          <input id='button-cadastro' className='button-active' type="submit" value="NOVO CADASTRO" onClick={() => alert('Enviado')} />
          <input id='button-limpar' className='button-active' onClick={apagaDados} value="LIMPAR FORMULÁRIO" />
        </form>
        <div className='blocks'>
        </div>

      </div>

      <div className='blocks'>
        <h1 className='label-title' id='user-list'>- Lista de Clientes -</h1>
        <p className='label-title' id='user-list'>Clique para</p>
        {(typeof dados.clientes === 'undefined') ? (
          <p id='user-list'>Carregando...</p>
        ) : (
          dados.clientes.map((cliente, i) => (
            <div>
              <form method="POST" action="/deletar">
                <input id='user-list' className='button-apagar' type="submit" value={cliente} name='cliente' ley={i} onClick={() => console.log({ cliente })} />
              </form>
            </div>
          ))
        )}
      </div>
    </div>

  )
}

export default App